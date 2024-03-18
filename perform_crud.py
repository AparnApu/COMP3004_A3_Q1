###############################################################################################
# Aparna Apu
# 101194937

# COMP 3005 A3 Q1

# https://www.psycopg.org/psycopg3/docs/basic/usage.html
# https://www.w3schools.com/sql/sql_update.asp
# https://www.w3schools.com/sql/sql_delete.asp
# https://www.psycopg.org/psycopg3/docs/basic/params.html
###############################################################################################

import psycopg

# Prompt fpr password to database
db_password = input("\nEnter your database password: ")

# These might change depending on your set-up
dbname = "School"
user = "postgres"
host = "localhost"
port = "5432"

# Connect to the "School" database
conn = psycopg.connect(f"dbname={dbname} user={user} host={host} port={port} password={db_password}")

###############################################################################################
# Initialize the database (tables and content)
###############################################################################################

def setupDatabase():

    # Cursor for database operations
    with conn.cursor() as cur:

        # Just to be safe
        cur.execute("DROP TABLE IF EXISTS students")

        # Define the table and its columns (the DDL)
        ddl = """ CREATE TABLE IF NOT EXISTS students
                    (student_id      SERIAL, 
                     first_name	     TEXT NOT NULL, 
                     last_name       TEXT NOT NULL,
                     email           TEXT NOT NULL UNIQUE, 
                     enrollment_date DATE,
                    
                     primary key (student_id)
                    ); """

        # Define the content of the table (the DML)
        dml = """ INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
                    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
                    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
                    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02'); """
        
        
        # Create the table
        cur.execute(ddl)

        # Populate the table
        cur.execute(dml)

        conn.commit() 

###############################################################################################
# Retrieves and displays all records from the students table
###############################################################################################

def getAllStudents():
    dql = "SELECT * FROM students"

    print("\nThe students are: \n")

    with conn.cursor() as cur:
        result = cur.execute(dql)

        for row in result:
            for item in row:
                print(item, end = '\t')
            print()
    
    print()

###############################################################################################
# Inserts a new student record into the students table
###############################################################################################
            
def addStudent(first_name, last_name, email, enrollment_date):
    dml = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"

    with conn.cursor() as cur:
        cur.execute(dml, ((first_name, last_name, email, enrollment_date)))
        conn.commit()    
    
    print("\n...New student " + first_name + " " + last_name + " added!\n")

###############################################################################################
# Updates the email address for a student with the specified student_id
###############################################################################################
    
def updateStudentEmail(student_id, new_email):
    dml = "UPDATE students SET email = %s WHERE student_id = %s"

    with conn.cursor() as cur:
        cur.execute(dml, (new_email, student_id))
        conn.commit();

    print("\n...Email updated for student ID " + student_id + "\n")

###############################################################################################
# Deletes the record of the student with the specified student_id
###############################################################################################
    
def deleteStudent(student_id):
    dml = "DELETE FROM students WHERE student_id = %s"

    with conn.cursor() as cur:
        cur.execute(dml, (student_id, ))
        conn.commit();

    print("\n...Student ID " + student_id + " was deleted\n")

###############################################################################################
# The main function
# Acts as the user interface
###############################################################################################
    
def main():

    setupDatabase()

    print("\nPopulating database ... Done\n")

    print("-" * 30)
    print("-" * 30)
    print("PERFORM CRUD")
    print("-" * 30)

    # Keep prompting an action until they exit (5)
    while True:
        print("-" * 30)
        print("\nWhat would you like to do today?")
        print("\t1. View All Students")
        print("\t2. Add New Student")
        print("\t3. Update Student Email")
        print("\t4. Delete Student")
        print("\t5. Exit")

        choice = input ("\nPlease make a choice between 1 and 5: ")

        print("-" * 30)

        # View All Students
        if choice == '1':
            getAllStudents()

        # Add New Student
        elif choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter an email: ")
            enroll_date = input("Enter date of enrollment (YYYY-MM-DD): ")

            # Error checking
            if (not first_name or not last_name or not email or not enroll_date):
                print("\nERR: No empty strings allowed!\n")
            else:
                try:
                    addStudent(first_name, last_name, email, enroll_date)
                except Exception as err:
                    print("\nERR: Please ensure that you have entered valid non-empty strings and the right date format!\n", err)
        
        # Update Student Email
        elif choice == '3':
            s_id = input("Enter a student ID: ")
            email = input("Enter an email: ")
            
            # Error checking
            if (not s_id or not email):
                print("\nERR: No empty strings allowed!\n")
            else:
                try:
                    updateStudentEmail(s_id, email)
                except Exception as err:
                    print("\nERR: Please ensure that you have entered valid non-empty strings!\n", err)
            
        # Delete Student
        elif choice == '4':
            s_id = input("Enter a student ID: ")
            
            # Error checking
            if (not s_id):
                print("\nERR: No empty strings allowed!\n")
            else:
                try:
                    deleteStudent(s_id)
                except Exception as err:
                    print("\nERR: Please ensure that you have entered valid non-empty strings!\n", err)
            

        # Exit
        elif choice == '5':
            conn.close()
            print("Exiting now ... Goodbye")
            break

        # Invalid choice
        else:
            print("ERR: Please enter a number between 1 and 5 inclusive!")

main()