import mysql.connector
from decouple import config

db = mysql.connector.connect(
    host= "yamanote.proxy.rlwy.net",        # atau IP server MySQL
    user="root",
    password=config("MYSQLPASSWORD"),
    database= config("MYSQLDATABASE"),
    port = config("MYSQLPORT")
)

cursor = db.cursor()
print("Connected!")