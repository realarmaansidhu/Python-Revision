# Python Code to implement the __eq__ method to compare two BankAccount objects based on their number attribute.

class BankAccount:
   # MODIFY to initialize a number attribute
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number
      
    def withdraw(self, amount):
        self.balance -= amount 
    
    # Define __eq__ that returns True if the number attributes are equal 
    def __eq__(self, other):
        return self.number == other.number   

# Create accounts and compare them       
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)

# Updated code for the __eq__ method to include a check for the type of the other object.

class BankAccount:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance
      
    def withdraw(self, amount):
        self.balance -= amount 

    # MODIFY to add a check for the type()
    def __eq__(self, other):
        return (self.number == other.number and type(self) == type(other))

acct = BankAccount(873555333)
pn = Phone(873555333)
print(acct == pn)