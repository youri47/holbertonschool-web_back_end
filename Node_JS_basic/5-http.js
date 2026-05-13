const http = require('http');
const countStudents = require('./3-read_file_async');

const DB_FILE = process.argv[2];

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    // On capture la sortie console.log produite par countStudents
    const lines = ['This is the list of our students'];
    const originalLog = console.log;
    console.log = (msg) => lines.push(msg);

    countStudents(DB_FILE)
      .then(() => {
        console.log = originalLog;
        res.end(lines.join('\n'));
      })
      .catch((err) => {
        console.log = originalLog;
        res.end(`This is the list of our students\n${err.message}`);
      });
  } else {
    res.end();
  }
});

app.listen(1245);

module.exports = app;
