import mysql.connector
import os

db = mysql.connector.connect(
    host= "yamanote.proxy.rlwy.net",        # atau IP server MySQL
    user="root",
    password="vdUUleETGAYacyXsNJJRTZcqNIEKDWoS",
    database="railway",
    port = "58251"
)

cursor = db.cursor()
print("Connected!")