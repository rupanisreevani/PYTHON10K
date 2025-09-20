import pymysql

try:
   
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='Srivani@123',
        port=3310
    )
    print('Connection successful')

except pymysql.MySQLError as err:
    print(f"Error: {err}")

finally:
    if conn:
        conn.close()
        print("Connection closed")
