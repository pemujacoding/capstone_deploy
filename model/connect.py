import mysql.connector
import os

db = mysql.connector.connect(
    host= "yamanote.proxy.rlwy.net",        # atau IP server MySQL
    user=os.getenv('MYSQLUSER'),
    password=os.getenv('MYSQLPASSWORD'),
    database=os.getenv('MYSQLDATABASE'),
    port = 58251
)

cursor = db.cursor()
print("Connected!")