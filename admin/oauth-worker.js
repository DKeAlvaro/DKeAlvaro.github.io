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
      const params = new URLSearchParams({
        client_id: env.GITHUB_CLIENT_ID,
        redirect_uri: url.origin + '/callback',
        scope: 'repo',
        response_type: 'code',
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
        return new Response('<html><body>No code</body></html>', {
          status: 200,
          headers: { 'Content-Type': 'text/html', ...corsHeaders },
        });
      }

      const r = await fetch('https://github.com/login/oauth/access_token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({
          client_id: env.GITHUB_CLIENT_ID,
          client_secret: env.GITHUB_CLIENT_SECRET,
          code,
        }),
      });

      const j = await r.json();

      if (!j.access_token) {
        return new Response('<html><body><h1>Error</h1><pre>' + JSON.stringify(j) + '</pre></body></html>', {
          status: 200,
          headers: { 'Content-Type': 'text/html', ...corsHeaders },
        });
      }

      const token = JSON.stringify(j.access_token).slice(1, -1);
      return new Response('<!DOCTYPE html><html><body><script>opener.postMessage("authorization:github:success:"+JSON.stringify({token:"' + token + '",provider:"github"}),"*");close();\x3c/script></body></html>', {
        status: 200,
        headers: { 'Content-Type': 'text/html; charset=utf-8', ...corsHeaders },
      });
    }

    return new Response('Not found', { status: 404, headers: corsHeaders });
  },
};
