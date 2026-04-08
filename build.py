import os
import sys


if os.path.exists('.git') and os.environ.get("APP_ENV") == "production":
    print("SECURITY CHECK FAILED!")
    print("Please do not keep the .git directory in the image!")
    sys.exit(1)

TEXT = """const http = require('http');

const port = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<p>Hello World</p>');
});

server.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
"""

if not os.path.exists('public'):
    os.mkdir('public')
with open('public/index.js', 'w') as f:
    f.write(TEXT)
