#patientID, firstName, lastName, birthday, email, password

import sqlite3

PatientLog = sqlite3.connect('PharmacyLogs/patientLog.db')

cursor = PatientLog.cursor()

cursor.execute("""CREATE TABLE patientLog (
                patientID text,
               firstName text,
               lastName text,
               birthday text,
               email text,
               password text
               )""")

PatientLog.commit()

PatientLog.close()