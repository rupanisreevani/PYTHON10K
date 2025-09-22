import pymysql
from db import info

try:
    pymysql.connect(**info)
    print("connection successful")
except:
    print("not able to connect")



