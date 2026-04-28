export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    if (path === '/auth') {
      const redirectUri = url.origin + '/callback';
      const params = new URLSearchParams({
        client_id: env.GITHUB_CLIENT_ID,
        redirect_uri: redirectUri,
        scope: 'repo,user',
      });
      const githubUrl = 'https://github.com/login/oauth/authorize?' + params.toString();
      return new Response('', {
        status: 302,
        headers: { Location: githubUrl, ...corsHeaders },
      });
    }

    if (path === '/callback') {
      const code = url.searchParams.get('code');
      if (!code) {
        return new Response('Missing code', { status: 400, headers: corsHeaders });
      }

      const tokenRes = await fetch('https://github.com/login/oauth/access_token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({
          client_id: env.GITHUB_CLIENT_ID,
          client_secret: env.GITHUB_CLIENT_SECRET,
          code,
        }),
      });

      const data = await tokenRes.json();
      const token = data.access_token;

      if (!token) {
        return new Response(JSON.stringify(data), {
          status: 400,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        });
      }

      const encoded = btoa(JSON.stringify({ token, provider: 'github' }));
      const html = `<!DOCTYPE html><html><body><script>
        opener.postMessage("authorization:github:success:" + atob("${encoded}"), "*");
        close();
      <\/script></body></html>`;

      return new Response(html, {
        status: 200,
        headers: { 'Content-Type': 'text/html; charset=utf-8', ...corsHeaders },
      });
    }

    return new Response('Not found', { status: 404, headers: corsHeaders });
  },
};
