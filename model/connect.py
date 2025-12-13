import mysql.connector
from decouple import config
import os

passs = os.getenv("MYSQL_PASSWORD")
db = mysql.connector.connect(
    host= "shuttle.proxy.rlwy.net",        # atau IP server MySQL
    user="root",
    password=passs,
    database= "railway",
    port = "53774"
)

cursor = db.cursor()
print("Connected!")