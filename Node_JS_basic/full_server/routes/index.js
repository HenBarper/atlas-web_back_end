import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

const express = require('express');

const router = express.Router();

router.get('/', AppController.index);

router.get('/students', StudentsController.getAllStudents);

router.get('/students/:major', StudentsController.getAllStudentsByMajor);

module.exports = router;
