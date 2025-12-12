import mysql.connector
import os

db = mysql.connector.connect(
    host= os.getenv('MYSQLHOST'),        # atau IP server MySQL
    user=os.getenv('MYSQLUSER'),
    password=os.getenv('MYSQLPASSWORD'),
    database=os.getenv('MYSQLDATABASE'),
    port=os.getenv('MYSQLPORT')
)

cursor = db.cursor()
print("Connected!")