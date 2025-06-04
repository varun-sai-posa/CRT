from db import connect 
def student_menu(book_id):
    while True:
        print("""\nstudent_menu
            1. view_library
            2. book_issued""")
        ch = input("enter the range")
        if ch == '1':
            view_library(book_id)
        elif ch == '2':
            book_issued(book_id)
            break
        else:
            print("invalid")
def view_library(book_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("select * from librarian")
    for row in cursor.fetchall():
        print(row)
    conn.close()
def book_issued(book_id):
    student_id = input("Enter your student ID: ")
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO student (student_id,book_id) VALUES (%s,%s)", (student_id,book_id))
    conn.commit()
    print(f"Book with ID {book_id} issued to student {student_id}.")
    conn.close()
student_menu('102')