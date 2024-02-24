const http = require('http');
const fs = require('fs');
// const countStudents = require('./3-read_file_async');

function countStudents(pathArg) {
  return new Promise((resolve, reject) => {
    try {
      const data = fs.readFileSync(pathArg, 'utf8');
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      console.log(`Number of students: ${lines.slice(1).length}`);

      const csStudents = [];
      const sweStudents = [];
      for (let i = 1; i < lines.length; i += 1) {
        const row = lines[i].split(',');
        if (row[3] === 'CS') {
          csStudents.push(row[0]);
        }
        if (row[3] === 'SWE') {
          sweStudents.push(row[0]);
        }
      }

      console.log(`Number of students in CS: ${csStudents.length}. List: ${csStudents.join(', ')}`);
      console.log(`Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.join(', ')}`);
      resolve();
    } catch (error) {
      reject(Error('Cannot load the database'));
    }
  });
}

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    console.log('This is the list of our students');
    countStudents(process.argv[2]);
    // console.log(process.argv[2]);
  }
});

app.listen(1245);

module.exports = app;
