import os
from pharmacist import Pharmacist
from verify import Verify

class Administrator(Verify):
    def create_pharmacist(self, pharmacistID, email, firstName, lastName, password):
        pharmacist = Pharmacist(pharmacistID, email, firstName, lastName, password)
        #have one func for pharmacist, import pharm data, export each log
        #csv row is pharmacsit, column is attributes
    def import_data:

    def export_logs:

