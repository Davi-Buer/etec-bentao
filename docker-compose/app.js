const http = require('http');
const { createClient } = require('redis');

const client = createClient({ url: process.env.REDIS_URL });
client.connect().then(() => console.log('Connected to Redis'));

const HTML = (messages, hits) => `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Docker Lab</title>
  <style>
    body { font-family: sans-serif; max-width: 600px; margin: 40px auto; padding: 0 16px; }
    input { width: 100%; padding: 8px; margin-bottom: 8px; box-sizing: border-box; }
    button { padding: 8px 16px; cursor: pointer; }
    li { padding: 6px 0; border-bottom: 1px solid #eee; }
    .hits { color: #888; font-size: 0.85em; margin-bottom: 16px; }
  </style>
</head>
<body>
  <h1>Docker Lab</h1>
  <p class="hits">Page visits: <strong>${hits}</strong></p>
  <input id="text" placeholder="Type a message..." />
  <button onclick="send()">Send</button>
  <ul>${messages.map(m => `<li>${m}</li>`).join('')}</ul>
  <script>
    async function send() {
      const text = document.getElementById('text').value.trim();
      if (!text) return;
      await fetch('/messages', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
      });
      location.reload();
    }
  </script>
</body>
</html>`;

const server = http.createServer(async (req, res) => {
  if (req.method === 'GET' && req.url === '/') {
    const hits = await client.incr('hits');
    const messages = await client.lRange('messages', 0, -1);
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(HTML(messages, hits));

  } else if (req.method === 'POST' && req.url === '/messages') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', async () => {
      const { text } = JSON.parse(body);
      await client.lPush('messages', text);
      res.writeHead(201);
      res.end('Created');
    });

  } else {
    res.writeHead(404);
    res.end('Not found');
  }
});

server.listen(3000, () => console.log('Server running on port 3000'));
