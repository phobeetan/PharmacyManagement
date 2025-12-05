import sqlite3

PharmacistLog = sqlite3.connect('PharmacyLogs/pharmacistLog.db')

cursor = PharmacistLog.cursor()

cursor.execute("""CREATE TABLE pharmacistLog (
                pharmacistID integer primary key,
                firstName text,
                lastName text,
                email text,
                password text
                )""")

def print_log():
    cursor.execute("SELECT  * FROM pharmacistLog")
    print(cursor.fetchall())

PharmacistLog.commit()

PharmacistLog.close()