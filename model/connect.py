import mysql.connector
from decouple import config

 # Ambil environment variable
db_user = config("MYSQLUSER")
db_pass = config("MYSQLPASSWORD")
db_name = config("MYSQLDATABASE")

# Validasi kalau ada yang belum di-set
missing = [k for k,v in {
    "MYSQLHOST": "yamanote.proxy.rlwy.net",
    "MYSQLPORT": 58251,
    "MYSQLUSER": db_user,
    "MYSQLPASSWORD": db_pass,
    "MYSQLDATABASE": db_name
}.items() if not v]

if missing:
    raise RuntimeError(f"Environment variable(s) missing: {', '.join(missing)}")

# Connect ke DB
db = mysql.connector.connect(
    host="yamanote.proxy.rlwy.net",
    port= 58251,
    user=db_user,
    password=db_pass,
    database=db_name
)

cursor = db.cursor