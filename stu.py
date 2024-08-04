import mysql.connector
from tabulate import tabulate

# Connect to MySQL
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2004",
    database="studentmanagement_database"
)

# Create a cursor object to execute queries
cursor = db_connection.cursor()

# Create a table for students
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS students_list (roll_no INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), dob DATE, department VARCHAR(255), phone_number VARCHAR(15), address TEXT, email VARCHAR(255), father_name VARCHAR(255), mother_name VARCHAR(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS students_mark (roll_no INT PRIMARY KEY,subject VARCHAR(225),CCET1 VARCHAR(10),CCET2 VARCHAR(10),GRADE VARCHAR(3))")

# Add a student to the database
def add_student(name, dob, department, phone_number, address, email, father_name, mother_name):
    sql = "INSERT INTO students_list (name, dob, department, phone_number, address, email, father_name, mother_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (name, dob, department, phone_number, address, email, father_name, mother_name)
    cursor.execute(sql, val)
    db_connection.commit()
    print("Student added successfully.")
    print("***************************************************************************************")

# Display all students
def display_students():
    cursor.execute("SELECT roll_no,name,dob,department,phone_number,address FROM students_list")
    students = cursor.fetchall()
    headers = ["Roll No", "Name", "DOB", "Department", "Phone Number", "Address"]
    print(tabulate(students, headers=headers, tablefmt="grid", numalign="center", stralign="center"))

# Search for a student by name
def search_student(name):
    sql = "SELECT * FROM students_list WHERE name = %s"
    val = (name,)
    cursor.execute(sql, val)
    student = cursor.fetchone()
    if student:
        headers = ["Roll No", "Name", "DOB", "Department", "Phone Number", "Address", "Email", "Father's Name", "Mother's Name"]
        print(tabulate([student], headers=headers, tablefmt="grid", numalign="center", stralign="center"))
    else: print("Student not found.")
    print("************************************************************************************")
# Update a student's information
def update_student(roll_no, new_name, new_dob, new_department, new_phone_number, new_address, new_email, new_father_name, new_mother_name):
    sql = "UPDATE students_list SET name = %s, dob = %s, department = %s, phone_number = %s, address = %s, email = %s, father_name = %s, mother_name = %s WHERE roll_no = %s"
    val = (new_name, new_dob, new_department, new_phone_number, new_address, new_email, new_father_name, new_mother_name, roll_no)
    cursor.execute(sql, val)
    db_connection.commit()
    print("Student information updated successfully.")
    print("**************************************************************************************")

# Delete a student from the database
def delete_student(roll_no):
    sql = "DELETE FROM students_list WHERE roll_no = %s"
    val = (roll_no,)
    cursor.execute(sql, val)
    db_connection.commit()
    print("Student deleted successfully.")
    print("**************************************************************************************")

#Update a student's Mark
def update_marks(roll_no,subject,CCET1,CCET2,GRADE):
    sql = "INSERT INTO students_mark (roll_no,subject,CCET1,CCET2,GRADE) VALUES (%s, %s, %s, %s, %s)"
    val = (roll_no,subject,CCET1,CCET2,GRADE)
    cursor.execute(sql, val)
    db_connection.commit()
    print("Student marks Added successfully.")

#Display Students Marks
def display_studentsmarks():
    cursor.execute("SELECT roll_no,subject,CCET1,CCET2,GRADE FROM students_mark")
    students = cursor.fetchall()
    headers = ["Roll No", "Subject", "CCET1", "CCET2", "GRADE"]
    print(tabulate(students, headers=headers, tablefmt="grid", numalign="center", stralign="center"))

# Delete Student Mark from table

def delete_studentmark(roll_no):
    sql = "DELETE FROM students_mark WHERE roll_no = %s"
    val = (roll_no,)
    cursor.execute(sql, val)
    db_connection.commit()
    print("Student deleted successfully.")
    print("***************************************************************************************")
    

# Main function
if __name__ == "__main__":
    create_table()

    while True:
        print("**************************************************************************************")
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Add Student Marks")
        print("7. Display Student Marks")
        print("8. Delete Student Marks")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            dob = input("Enter student DOB (YYYY-MM-DD): ")
            department = input("Enter student department: ")
            phone_number = input("Enter student phone number: ")
            address = input("Enter student address: ")
            email = input("Enter student email: ")
            father_name = input("Enter student father's name: ")
            mother_name = input("Enter student mother's name: ")
            add_student(name, dob, department, phone_number, address, email, father_name, mother_name)
        elif choice == "2":
            display_students()
        elif choice == "3":
            name = input("Enter student name to search: ")
            search_student(name)
        elif choice == "4":
            roll_no = input("Enter student roll number to update: ")
            new_name = input("Enter new name: ")
            new_dob = input("Enter new DOB (YYYY-MM-DD): ")
            new_department = input("Enter new department: ")
            new_phone_number = input("Enter new phone number: ")
            new_address = input("Enter new address: ")
            new_email = input("Enter new email: ")
            new_father_name = input("Enter new father's name: ")
            new_mother_name = input("Enter new mother's name: ")
            update_student(roll_no, new_name, new_dob, new_department, new_phone_number, new_address, new_email, new_father_name, new_mother_name)
        elif choice == "5":
            roll_no = input("Enter student roll number to delete: ")
            delete_student(roll_no)
        elif choice=="6":
            roll_no=input("Enter student roll number to update marks:")
            subject=input("Enter the subject:")
            CCET1=int(input("Enter the CCET1 mark:"))
            CCET2=int(input("Enter the CCET2 mark:"))
            GRADE=input("Enter the Grade:")
            update_marks(roll_no,subject,CCET1,CCET2,GRADE)
        elif choice=="7":
            display_studentsmarks()
        elif choice == "8":
            roll_no = input("Enter student roll number to delete: ")
            delete_studentmark(roll_no)
        elif choice == "9":
            print("Thank you")
            break
        else:
            print("Invalid choice. Please try again.")
