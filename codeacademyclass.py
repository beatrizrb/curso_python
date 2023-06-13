class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    print(f'Voce passou pelo self id')
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

# Write your code below
class Admin(Employee, User):
  def __init__(self):
    Employee.__init__(self)
    print(self.id)
    User.__init__(self, self.id, "Admin")
    

  def say_id(self):
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
#print(e3.id)
#print(e2.id)
e3.say_user_info()