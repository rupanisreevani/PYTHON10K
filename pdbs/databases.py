import pymysql
#connect to mtsql
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='Srivani@123',
    port=3310
    
)

cursor = conn.cursor()

# 2. Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS coders10000")

# 3. Use that database
cursor.execute("USE coders10000")

# 4. Create table students
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    course VARCHAR(100),
    marks INT
)
""")

print(" Database 'coders10000' and table 'students' created successfully!")

cursor.close()
conn.close()

#insert at least 5 records
students=[1,'sreevani','f','9874563214','']