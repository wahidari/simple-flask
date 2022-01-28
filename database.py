import mysql.connector

# Set up & Open database connection
db = mysql.connector.connect(user='root',
                             password='',
                             host='127.0.0.1',
                             database='flask')

# Cek if Database is Connected
if db.is_connected():
    print("Database Connected !")

def getTabelUsers():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `users`")
    datatabelusers = cursor.fetchall()
    return datatabelusers
