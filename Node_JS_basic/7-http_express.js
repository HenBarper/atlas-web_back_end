const express = require('express');
const fs = require('fs').promises;

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

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const theData = await countStudents(process.argv[2]);
  res.send(`${theData}`);
});

app.listen(port, () => {
  console.log(`Listening on port ${port}.`);
});

module.exports = app;
