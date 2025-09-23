import pymysql
from db import info

try:
    conn=pymysql.connect(**info)
    print("connection successful")
except:
    print("not able to connect")

cursor=conn.cursor()


#to create database
query='create database  if not exists  10000coders'
cursor.execute(query)
#using database 
cursor.execute('use  10000coders')
#creating a table with id ,name,email,course,joined_date
# try:
#     create_table = """CREATE TABLE IF NOT EXISTS student_new(
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     email VARCHAR(100),
#     course VARCHAR(100),
#     joined_date DATE
# );"""

#     cursor.execute(create_table)
# except: 
#     print('something went wrong')
#insert single row id data
# def insertsinglerow(data):
#     try:
#         insertdata = """INSERT INTO student 
#         (name, email, course, joined_date) 
#         VALUES (%s, %s, %s, %s)"""
    
#         cursor.execute(insertdata, data)
        
#         print("Data inserted")
#     except Exception as e:
#         print("Something went wrong:", e)


# insertsinglerow(('tharun','tharun@gamil.com','pfs','2025-02-02'))
# insertsinglerow(('vani','vani@gamil.com','pfs','2025-04-23'))

#insert multiple rowr at a time

# def insertmultiplerow(data):
#     try:
    
#         insertquery=""" insert into student (name,email,course,joined_date) values (%s,%s,%s,%s) """
#         cursor.executemany(insertquery, data)   
    
#         print("Data inserted successfully")
#     except Exception as e:
#         print("Something went wrong:", e)

# insertmultiplerow([('nani','nani@gmail.com','pfs','2025-03-04'),('manasa','manasa@gmail.com','pfs','2025-09-23')])


# def getrecords():
#     try:
#         query='select * from student'
#         cursor.execute(query)
#         results=cursor.fetchall()
#         for row in results:
#             print(row)
#     except Exception as e:
#         print('error occurred')
# getrecords()
# def getrecordsofstudentofsamecourse():

# def getstudentbycourse(course_name)
#update record
def updaterecordsemail(student_id, new_email):
    try:
        query = """UPDATE student SET email=%s WHERE id=%s"""
        cursor.execute(query, (new_email, student_id))
        conn.commit()   
        print(f"Student ID {student_id} email updated to {new_email}")
    except Exception as e:
        print("Something went wrong:", e)

updaterecordsemail(1, "abcd@gmail.com")
#deleting a record by email:

def deletestudentemail(email):
    try:
        query = """delete from student  WHERE email=%s """
        cursor.execute(query, (email))
        conn.commit()   
        print(f"REcord with email {email} deleted successfully")
    except Exception as e:
        print("Something went wrong:", e)


deletestudentemail( "nani@gmail.com")
#deleting a record by name
def deletestudentname(name):
    try:
        query = """delete from student  WHERE name=%s """
        cursor.execute(query, (name))
        conn.commit()   
        print(f"REcord with name {name} deleted successfully")
    except Exception as e:
        print("Something went wrong:", e)


deletestudentname( "sai")



conn.commit()
cursor.close()
conn.close()
