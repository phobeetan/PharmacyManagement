import sqlite3

PatientLog = sqlite3.connect('PharmacyLogs/patientLog.db')

cursor = PatientLog.cursor()

cursor.execute("""CREATE TABLE patientLog (
                patientID integer primary key,
                firstName text,
                lastName text,
                birthday text,
                email text,
                password text
                )""")

def add_patient(Patient):
    with PatientLog:
        cursor.execute("INSERT INTO patientLog VALUES (:patientID, :firstName, :lastName, :birthday, :email, :password)",
                    {'patientID': None, 'firstName': Patient.firstName, 'lastName': Patient.lastName,
                        'birthday': Patient.birthday, 'email': Patient.email, 'password': Patient.password})    

def print_log():
    cursor.execute("SELECT  * FROM patientLog")
    print(cursor.fetchall())

PatientLog.commit()

PatientLog.close()