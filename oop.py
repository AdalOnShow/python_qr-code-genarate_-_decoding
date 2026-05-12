# Object-Oriented Programming (OOP) in Python
# OOP is a programming paradigm that organizes code into objects, which are instances of classes. A class is a blueprint for creating objects, and it defines the properties (attributes) and behaviors (methods) that the objects will have.
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