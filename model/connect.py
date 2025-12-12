import mysql.connector

db = mysql.connector.connect(
    host="yamanote.proxy.rlwy.net",        # atau IP server MySQL
    port = "58251",
    user="root",
    password="vdUUleETGAYacyXsNJJRTZcqNIEKDWo",
    database="railway"
)

cursor = db.cursor()
print("Connected!")