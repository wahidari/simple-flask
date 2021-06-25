import mysql.connector

# Set up & Open database connection
db = mysql.connector.connect(user='root',
                             password='',
                             host='127.0.0.1',
                             database='datates')

# Cek if Database is Connected
if db.is_connected():
    print("Database Connected !")

def getTabelBerita():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `tb_berita`")
    datatabelberita = cursor.fetchall()
    return datatabelberita
