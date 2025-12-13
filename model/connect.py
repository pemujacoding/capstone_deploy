import mysql.connector
from decouple import config
import os

passs = os.getenv("MYSQL_PASSWORD")
db = mysql.connector.connect(
    host= "yamanote.proxy.rlwy.net",        # atau IP server MySQL
    user="root",
    password="vdUUleETGAYacyXsNJJRTZcqNIEKDWoS",
    database= "railway",
    port = "58251"
)

cursor = db.cursor()
print("Connected!")