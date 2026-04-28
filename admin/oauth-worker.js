// Decap CMS GitHub OAuth Gateway
// Deploy this as a Cloudflare Worker.
// Environment variables (set in Cloudflare dashboard):
//   GITHUB_CLIENT_ID     — from GitHub OAuth App
//   GITHUB_CLIENT_SECRET — from GitHub OAuth App

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
      const githubAuthUrl = new URL('https://github.com/login/oauth/authorize');
      githubAuthUrl.searchParams.set('client_id', env.GITHUB_CLIENT_ID);
      githubAuthUrl.searchParams.set('redirect_uri', redirectUri);
      githubAuthUrl.searchParams.set('scope', 'repo,user');
      return Response.redirect(githubAuthUrl.toString(), 302);
    }

    if (path === '/callback') {
      const code = url.searchParams.get('code');
      if (!code) {
        return new Response('Missing code parameter', { status: 400 });
      }

      const tokenResponse = await fetch('https://github.com/login/oauth/access_token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({
          client_id: env.GITHUB_CLIENT_ID,
          client_secret: env.GITHUB_CLIENT_SECRET,
          code,
        }),
      });

      const tokenData = await tokenResponse.json();
      const accessToken = tokenData.access_token;

      if (!accessToken) {
        return new Response(JSON.stringify(tokenData), {
          status: 400,
          headers: { 'Content-Type': 'application/json', ...corsHeaders },
        });
      }

      const script = `
        <script>
          (function() {
            var authResult = ${JSON.stringify({ token: accessToken, provider: 'github' })};
            window.opener.postMessage(
              'authorization:github:success:${JSON.stringify(authResult)}',
              'https://dkealvaro.github.io'
            );
            window.close();
          })();
        </script>
      `;
      return new Response(script, {
        headers: { 'Content-Type': 'text/html', ...corsHeaders },
      });
    }

    return new Response('Not found. Use /auth to start OAuth.', { status: 404 });
  },
};
