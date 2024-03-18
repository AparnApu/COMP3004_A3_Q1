# COMP 3005 Winter 2024
#### Assignment 3, Question 1
#### Aparna Apu, 101194937

## Introduction
It is a Python application that connects to a PostgreSQL database (School) and performs specific CRUD (Create, Read, Update, Delete) operations.
- getAllStudents(): Retrieves and displays all records from the students table.
- addStudent(first_name, last_name, email, enrollment_date): Inserts a new student record into the students table.
- updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id.
- deleteStudent(student_id): Deletes the record of the student with the specified student_id.

## Instructions
1. Create a database "School" in PostgreSQL.
    1. You may populate it, but the program will write over it!

2. Install `psycopg` in your terminal
    1. Ensure you have installed `python` (`python3 --version`)
    2. Ensure you have updated your `pip` (`pip install --upgrade pip`)
    3. Now run `pip install "psycopg[binary]"`
  
3. In the source code (`perform_crud.py`), edit the setup variables (lines 19 - 22) to suit your setup.
    1. You will be prompted for a password later when running the program
  
4. Run the code via the command `python3 perform_crud.py`.
    1. Enter your password
  
5. Now, you can use the command-line prompts and user interface to perform various CRUD operations.

## Video Demonstration
https://youtu.be/g3haNKlnqFc
