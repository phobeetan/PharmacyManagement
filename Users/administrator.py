import csv
import os
import sqlite3
import bcrypt
from pharmacist import Pharmacist
from verify import Verify
from PharmacyLogs import pharmacistLog, patientLog, logSet, inventoryLog, pickUpLog, prescriptionLog

class Administrator(Verify):
    def create_pharmacist(self, pharmacistID, email, firstName, lastName, password):
        pharmacist = Pharmacist(pharmacistID, email, firstName, lastName, password)
    def import_data(self, csv_paths: list[str]):
        csv_to_db = {
        "pharmacistLog.csv" : "pharmacistLog.db",
        "patientLog.csv" : "patientLog.db",
        "pickUpLog.csv" : "pickUpLog.db",
        "prescriptionLog.csv" : "prescriptionLog.db",
        "logSet.csv" : "logSet.db",
        "inventoryLog.csv" : "inventoryLog.db"
        }

        for csv_path in csv_paths:
            csv_name = os.path.basename(csv_path)

            if csv_name not in csv_to_db:
                raise ValueError (f"No database found for {csv_name}")
            db_path = csv_to_db[csv_name]

            with open (csv_path, newline = "", encoding = "utf-8") as csv_file:
                reader = csv.reader(csv_file)
                headers = next(reader)
            placeholders = ", ".join("?" for _ in headers)
            columns = ", ".join(headers)

            with sqlite3.connect(db_path) as connect:
                cursor = connect.cursor()
                for row in reader:
                    cursor.execute(
                        f"""
                                       INSERT INTO log ({columns})
                                       VALUES ({placeholders})
                                       """,
                        row
                    )
                connect.commit()


    def export_logs(self):
        db_paths = [
            "pharmacistLog.db",
            "patientLog.db",
            "pickUpLog.db",
            "logSet.db",
            "inventoryLog.db"
        ],
        out_csv_paths = [
            "pharmacistLog.csv",
            "patientLog.csv",
            "pickUpLog.csv",
            "logSet.csv",
            "inventoryLog.csv"
        ]

        for db_path, csv_path in zip(db_paths, out_csv_paths):
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM log")
                rows = cursor.fetchall()
            with open(csv_path, 'w', newline='', encoding = "utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow()

    )



