# class User:
#   def __init__(self,username, email, password):
#     self.username = username
#     self._email = email
#     self.password = password

#   @property
#   def email(self):
#     print("Getting email...")
#     return self._email
#   @email.setter
#   def email(self, new_email):
#     print("Setting email...")
#     if "@" in new_email:
#       self._email = new_email
#     else:
#       print("Invalid email address")


# user1 = User("john", "john@example.com", "password123")
# user1.email = "this is not a valid@ email"
# print(user1.email)

# class User:
#   user_count = 0

#   def __init__(self, username, email, password):
#     self.username = username
#     self._email = email
#     self.password = password
#     User.user_count += 1

#   def display_user_info(self):
#     print(f"Username: {self.username}, Email: {self._email}")

# user1 = User("john", "john@example.com", "password123")
# print(f"Total users: {User.user_count}")
# user2 = User("jane", "jane@example.com", "password456")
# print(f"Total users: {User.user_count}")

class BankAccount:
  MIN_BALANCE = 100

  def __init__(self, owner, balance = 0):
    self.owner = owner
    self._balance = balance

  def deposit(self, amount):
    if amount > 0:
      self._balance += amount
      print(f"Deposited ${amount}. New balance: ${self._balance}")  
    else:
      print("Deposit amount must be positive")
    
  @staticmethod 
  def is_valid_interest_rate(rate):
    return 0 <= rate <= 5

account1 = BankAccount("Alice", 500)
account1.deposit(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(13))