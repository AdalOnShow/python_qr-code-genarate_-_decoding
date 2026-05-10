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


user1 = User("john", "john@example.com", "password123")
user1.email = "this is not a valid@ email"
print(user1.email)

