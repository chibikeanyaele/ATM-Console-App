class cardHolder():
    def __init__(self, cardNum, pin, firstname, lastname, balance):
       self.cardNum = cardNum
       self.pin = pin
       self.firstname = firstname
       self.lastname = lastname
       self.balance = balance

       ### Getter Methods
       def get_cardNum(self):
           return self.cardNum
       def get_pin(self):
           return self.pin
       def get_firstName(self):
           return self.firstname
       def get_lastName(self):
           return self.lastname
       def get_balance(self):
           return self.balance

       ### Setter methods
       def set_cardNum(self, newVal):
           self.cardNum = newVal
       def set_pin(self, newVal):
           self.pin = newVal
       def set_firstname(self, newVal):
           self.firstName = newVal
       def set_lastname(self, newVal):
           self.lastName = newVal
       def set_balance(self, newVal):
           self.balance = newVal

       def print_out(self):
           print("Card #: ", self.cardNum)
           print("Pin: ", self.pin)
           print("First Name: ", self.firstname)
           print("Last Name: ", self.lastname)
           print("Balance: ", self.balance)
