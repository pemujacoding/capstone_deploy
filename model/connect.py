import mysql.connector
from decouple import config

passs = config("MYSQL_ROOT_PASSWORD")
db = mysql.connector.connect(
    host= "yamanote.proxy.rlwy.net",        # atau IP server MySQL
    user="root",
    password=passs,
    database= "railway",
    port = "58251"
)

cursor = db.cursor()
print("Connected!")