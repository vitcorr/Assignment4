import psycopg2

#user credentials
datab = input("Enter database name: ")
pas = input("Enter your database password: ")
hos = input("Enter database host: ")


def connect():
    try:
        conn = psycopg2.connect(
            user = "postgres",
            password = pas,
            host = hos,
            port = "5432",
            database = datab
        )
        return conn

    except Exception as error:
        print("Error connecting to database")
        print(error)

#Retrieves and displays all records from the students table
def getAllStudents():
    conn = connect()
    if conn:
        try:
            curr = conn.cursor()
            curr.execute("SELECT * FROM students;")
            for foo in curr.fetchall():
                print(foo)
        
        except Exception as error:
            print("Unable to retrieve students")
            print(error)
        finally:
            conn.close()

#Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect()
    if conn:
        try:
            curr = conn.cursor()
            insert_script = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES(%s,%s,%s,%s);"
            insert_value = (first_name, last_name, email, enrollment_date)
            curr.execute(insert_script, insert_value)
            conn.commit()
            print("Student added sucessfully")
        
        except Exception as error:
            print("Unable to add student")
            print(error)
        finally:
            conn.close()

# Updates the email address for a student with the specified student_id.    
def updateStudentEmail(student_id, new_email):
    conn = connect()
    if conn:
        try:
            curr = conn.cursor()
            insert_script = "UPDATE students SET email = %s WHERE student_id = %s;"
            insert_value = (new_email, student_id)
            curr.execute(insert_script, insert_value)
            conn.commit()
            print("Student email updated succesfully")
        
        except Exception as error:
            print("Unable to update email")
            print(error)
        finally:
            conn.close()

#Deletes the record of the student with the specified student_id.
def deleteStudent(student_id): 
    conn = connect()
    if conn:
        try:
            curr = conn.cursor()
            insert_script = "DELETE FROM students WHERE student_id = %s;"
            insert_value = (student_id,)
            curr.execute(insert_script, insert_value)
            conn.commit()
            print("Student record deleted succesfully")
        
        except Exception as error:
            print("Unable to delete student record")
            print(error)
        finally:
            conn.close()

# test
# getAllStudents()
# addStudent('vic', 'kol', 'MEEEE.kol@example.com', '2023-02-02')
# updateStudentEmail(4, "updated.email@example.com")
# deleteStudent(4)

def main():
    

    while True:
        print("Select an option\n")
        print("1 = get all student records")
        print("2 = insert new student record")
        print("3 = update student email")
        print("4 = delete the student record")
        print("q = exit program\n")
        option = input("Enter your option: ")

        if option == "1":
            getAllStudents()
            print("\n")
        elif option == "2":
            first_name = input("Enter firstname: ") 
            last_name = input("Enter lastname: ")
            email = input("Enter email: ") 
            enrollment_date = input("Enter enrollment date(yyyy-mm-dd): ") 
            addStudent(first_name, last_name, email, enrollment_date)
            print("\n")
        elif option == "3":
            student_id = input("Enter student ID: ") 
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
            print("\n")
        elif option == "4":
            student_id = input("Enter ID to be deleted: ") 
            deleteStudent(student_id)
            print("\n")
        elif option == "q":
            break



if __name__ == '__main__':
    main()