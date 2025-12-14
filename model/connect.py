import os
import mysql.connector
from urllib.parse import urlparse

database_url = os.getenv("MYSQL_URL")

url = urlparse(database_url)

db = mysql.connector.connect(
    host=url.hostname,
    user=url.username,
    password=url.password,
    database=url.path.lstrip("/"),
    port=url.port,
)

cursor = db.cursor()
print("Connected!")