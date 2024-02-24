const http = require('http');
// const fs = require('fs');
const fs = require('fs').promises;
// const countStudents = require('./3-read_file_async');

async function countStudents(pathArg) {
  try {
    const data = await fs.readFile(pathArg, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    let returnString = 'This is the list of our students\n';
    returnString += `Number of students: ${lines.slice(1).length}\n`;

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

    returnString += `Number of students in CS: ${csStudents.length}. List: ${csStudents.join(', ')}\n`;
    returnString += `Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.join(', ')}`;
    return (returnString);
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    const theData = await countStudents(process.argv[2]);
    res.end(`${theData}`);
  }
});

app.listen(1245);

module.exports = app;
