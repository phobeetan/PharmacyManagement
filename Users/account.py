import validators

class Account():
    
    def __init__(email, password):
        self.email = self.validateEmail(email)
        self.firstName = self.validateName(firstName)
        self.lastName = self.validateName(lastName)
        self.verifyLogin()
        if verify == False: 
            return "Your email or password is invaild."
        self.editUser()
    
    def validateEmail(email):
        if self.validators.email(email):
            return email
        else:
            return "Please enter a valid email."

    def validateName(name):
        validate = False
        chars = "@0123456789~``!@#$%^&*()_+=[]\{}|:<>?,./"
        for x in self.name:
            if x in chars:
                validate = False
        validate = True
        if validate == True:
            return name
        else:
            return "Please enter a valid name"

    def verifyLogin(log, email, password):
        verify = (password == getUserPassword(getUserID))
    
    def editUser(log, email, firstName, lastName):
        if self.validateName(firstName) == firstName:
            self.firstName = firstName
        else:
            return "Please enter a valid first name."
        if self.validateName(lastName) == lastName:
            self.lastName = lastName
        else:
            return "Please enter a valid last name."
        if self.validateEmail(email) == email:
            self.email = email
        else:
            return "Please enter a valid email."
    






