// Using the database database.csv (provided in project description), create a function countStudents in the file 2-read_file.js

// Create a function named countStudents. It should accept a path in argument
// The script should attempt to read the database file synchronously
// If the database is not available, it should throw an error with the text Cannot load the database
// If the database is available, it should log the following message to the console Number of students: NUMBER_OF_STUDENTS
// It should log the number of students in each field, and the list with the following format: Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES
// CSV file can contain empty lines (at the end) - and they are not a valid student!

const fs = require('fs');
const path = require('path');

function countStudents(pathArg) {
    fs.readFile(path.join(__dirname, pathArg), 'utf8', (err, data) => {
        if (err) {
            console.error("Cannot load the database");
        } else {
            const lines = data.split('\n').filter(line => line.trim() !== '');
            console.log(`Number of students: ${lines.slice(1).length}`);

            let cs_students = []
            let swe_students = []
            for( let i = 1; i < lines.length; i++) {
                const row = lines[i].split(',');
                if(row[3] === 'CS') {
                    cs_students.push(row[0]);
                }
                if(row[3] === 'SWE') {
                    swe_students.push(row[0]);
                }
            }
              
            console.log(`Number of students in CS: ${cs_students.length}. List: ${cs_students.join(', ')}`);
            console.log(`Number of students in CS: ${swe_students.length}. List: ${swe_students.join(', ')}`);
        }
    })
}

module.exports = countStudents;