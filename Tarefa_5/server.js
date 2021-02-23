const http = require('http');

const requestListener = function (req, res) {
  res.writeHead(200);
  res.end('Esse é um servidor feito com Node.js');
}

const server = http.createServer(requestListener);
server.listen(8080);