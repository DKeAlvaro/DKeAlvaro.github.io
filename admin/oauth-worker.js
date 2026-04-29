export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    if (path === '/auth') {
      const p = new URLSearchParams({
        client_id: env.GITHUB_CLIENT_ID,
        scope: 'repo',
        response_type: 'code',
      });
      return Response.redirect('https://github.com/login/oauth/authorize?' + p.toString(), 302);
    }

    if (path === '/callback') {
      const code = url.searchParams.get('code');
      const r = await fetch('https://github.com/login/oauth/access_token', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json', 
          'Accept': 'application/json',
          'User-Agent': 'Cloudflare-Worker'
        },
        body: JSON.stringify({
          client_id: env.GITHUB_CLIENT_ID,
          client_secret: env.GITHUB_CLIENT_SECRET,
          code,
        }),
      });
      const j = await r.json();

      let status;
      let msgContent;
      if (j.error || !j.access_token) {
        status = 'error';
        msgContent = { error: j.error || 'no token', provider: 'github' };
      } else {
        status = 'success';
        msgContent = { token: j.access_token, provider: 'github' };
      }

      const safeMsgContent = JSON.stringify(msgContent);

      const html = `<!DOCTYPE html><html><body><script>
        (function() {
          function receiveMessage(e) {
            // Send token back to the main CMS window securely
            window.opener.postMessage(
              "authorization:github:${status}:" + JSON.stringify(${safeMsgContent}),
              e.origin
            );
            window.removeEventListener("message", receiveMessage, false);
          }
          window.addEventListener("message", receiveMessage, false);
          // Notify the CMS that authorization is starting
          window.opener.postMessage("authorizing:github", "*");
        })();
      </script></body></html>`;

      return new Response(html, { headers: { 'Content-Type': 'text/html' } });
    }

    return new Response('', { status: 404 });
  },
}
