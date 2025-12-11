from verify import Verify
from PharmacyLogs.patientLog import patientLog

log = patientLog()

class Patient(Verify):
    def __init__(self, email, firstName, lastName, birthday, password):
        self.log = log
        self.verify = Verify(log.DB_PATH)
        self.email = email

        # Validate
        if not self.verify.validateEmail(email):
            raise ValueError("Email Already Exists")
        if not self.verify.validateName(firstName) or not self.verify.validateName(lastName):
            raise ValueError("Invalid Characters in Name")
        
        # Register
        self.log.insert(email, firstName, lastName, birthday, password)
    
    def verifyLogin(self, email, password):
        return self.verify.validateEmail(email, password)

