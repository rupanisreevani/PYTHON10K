import mysql.connector

try:
    print("Trying connection...")
    mysql.connector.connect(
        host='localhost',
        user='root',
        password='Srivani@123',
        port=3310
    )
   
    print('Connection successful')
except:
    print(f"Error: {e}")
