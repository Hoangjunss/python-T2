-- Active: 1704807633484@@127.0.0.1@3306@student_information_management
USE student_information_management;

SELECT * FROM department dp INNER JOIN schedule sh ON dp.id = sh.`departmentID`
        INNER JOIN semester ss on ss.id = sh.`semesterID`
        