class Animal:
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return f'{self.name!r}'
 
  def __add__(self, another_animal):
    # criando um novo objeto
    return Animal(self.name + another_animal.name)
 
a1 = Animal("Horse")
a2 = Animal("Penguin")
a3 = a1 + a2
print(a1) # Prints "Horse"
print(a2) # Prints "Penguin"
print(a3) # Prints "HorsePenguin"
print(type(a3))