# Object-Oriented Programming (OOP) in Python
# OOP is a programming paradigm that organizes code into objects, which are instances of classes. A class is a blueprint for creating objects, and it defines the properties (attributes) and behaviors (methods) that the objects will have.
from qrcode import make


class User:
  def __init__(self,username, email, password):
    self.username = username
    self._email = email
    self.password = password

  @property
  def email(self):
    print("Getting email...")
    return self._email
  @email.setter
  def email(self, new_email):
    print("Setting email...")
    if "@" in new_email:
      self._email = new_email
    else:
      print("Invalid email address")


# user1 = User("john", "john@example.com", "password123")
# user1.email = "this is not a valid@ email"
# print(user1.email)

# In the above code, we have defined a User class with an __init__ method that initializes the username, email, and password attributes. We have also defined a property for the email attribute, which allows us to control how the email is accessed and modified. The email setter checks if the new email address contains an "@" symbol before updating the _email attribute.
class User:
  user_count = 0

  def __init__(self, username, email, password):
    self.username = username
    self._email = email
    self.password = password
    User.user_count += 1

  def display_user_info(self):
    print(f"Username: {self.username}, Email: {self._email}")

# user1 = User("john", "john@example.com", "password123")
# print(f"Total users: {User.user_count}")
# user2 = User("jane", "jane@example.com", "password456")
# print(f"Total users: {User.user_count}")

# In this code, we have added a class variable user_count to keep track of the number of User instances created. Each time a new User is initialized, we increment the user_count by 1. We also have a method display_user_info that prints the username and email of the user.
class BankAccount:
  MIN_BALANCE = 100

  def __init__(self, owner, balance = 0):
    self.owner = owner
    self._balance = balance

  def deposit(self, amount):
    if self._is_valid_deposit(amount):
      self._balance += amount
      self.__log_transaction("deposit", amount)
    else:
      print("Deposit amount must be positive")

  def _is_valid_deposit(self, amount):
    return amount > 0
  
  def __log_transaction(self, transaction_type, amount):
    print(f"Logging {transaction_type} of ${amount}. New balance: ${self._balance}")

  @staticmethod 
  def is_valid_interest_rate(rate):
    return 0 <= rate <= 5

# account1 = BankAccount("Alice", 500)
# account1.deposit(200)

# print(BankAccount.is_valid_interest_rate(3))
# print(BankAccount.is_valid_interest_rate(13))

#! Encapsulation is the principle of hiding the internal state and behavior of an object and only exposing a public interface. This is often achieved using private attributes and methods, which are denoted by a leading underscore (_). In the BankAccount class, we have made the balance attribute private by prefixing it with an underscore. We also have a public method deposit that allows us to modify the balance, but we control how it can be modified through the _is_valid_deposit method. Additionally, we have a private method __log_transaction that is used to log transactions whenever a deposit is made.
class BankAccount:
  def __init__(self):
    self._balance = 0.0

  @property
  def balance(self):
    return self._balance
  
  def deposit(self, amount):
    if amount > 0:
      self._balance += amount
    else:
      raise ValueError("Deposit amount must be positive.")

  def withdraw(self, amount):
    if amount > self._balance:
      raise ValueError("Insufficient funds.")
    elif amount <= 0:
      raise ValueError("Withdrawal amount must be positive.")
    else:
      self._balance -= amount

# account = BankAccount()
# print(account.balance) # Output: 0.0
# account.deposit(100)
# print(account.balance) # Output: 100.0
# account.withdraw(30)
# print(account.balance) # Output: 70.0


#! Abstraction is the principle of hiding complex implementation details and exposing only the necessary features of an object. In the BankAccount class, we have abstracted away the internal workings of how the balance is managed and how transactions are logged. The user of the BankAccount class does not need to know how the balance is stored or how transactions are logged; they only need to interact with the public methods deposit and withdraw to manage their account balance.

class EmailService:
  def _connect(self):
    print("Connecting to email server...")
  def _authenticate(self):
    print("Authenticating...")

  def sendEmail(self):
    self._connect()
    self._authenticate()
    print("Sending email...")
    self._disconnect()

  def _disconnect(self):
    print("Disconnecting from email server...")


# email = EmailService()
# email.sendEmail()

#! Inheritance is a fundamental principle of OOP that allows a new class (called a child or subclass) to inherit properties and behaviors from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.

class Vehicle:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def start_engine(self):
    print("Engine started....")

  def stop_engine(self):
    print("Engine stopped!")

class Car(Vehicle):
  def __init__(self, brand, model, year, num_doors, num_wheels=4):
    super().__init__(brand, model, year)
    self.num_doors = num_doors
    self.num_wheels = num_wheels

  def honk(self):
    print("Honk! Honk!")

class Bike(Vehicle):
  def __init__(self, brand, model, year, has_pedals=False, num_wheels=2):
    super().__init__(brand, model, year)
    self.has_pedals = has_pedals
    self.num_wheels = num_wheels

  def ring_bell(self):
    print("Ring! Ring!")

# car = Car("Toyota", "Camry", 2020, 4)
car = Car("Toyota", "Camry", 2020, 4)

# bike = Bike("Trek", "Marlin 7", 2021, has_pedals=True)
bike = Bike("Trek", "Marlin 7", 2021, has_pedals=True)

print(car.__dict__)
print(bike.__dict__)