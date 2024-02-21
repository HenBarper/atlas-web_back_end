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
            // console.log(" Number of students: " + data);

            const lines = data.split('\n').filter(line => line.trim() !== '');
            console.log(`Number of students: ${lines.slice(1).length}`);
            // console.log(lines);
            let csData = lines.filter((line) => {
                let fields = line.split(',');
                return fields[3] === 'CS';
            });
            let sweData = lines.filter((line) => {
                let fields = line.split(',');
                return fields[3] === 'SWE';
            });
              
            console.log(`Number of students in CS: ${csData.length}`);
            console.log(`Number of students in CS: ${sweData.length}`);
            // const students = {
            //     CS: [],
            //     SWE: []
            // };

            // for (const line of lines) {
            //     const [firstName, , field] = line.split(',');
            //     if (field && field.trim() in students) {
            //         students[field.trim()].push(firstName.trim());
            //     }
            // }
            // console.log(`Number of students: ${lines.length}`);
            // for (const field in students) {
            //     console.log(`Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`);
            // }
        }
    })
}

module.exports = countStudents;