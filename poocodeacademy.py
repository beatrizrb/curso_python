class User:
  def __init__(self):
    self._username = None

  @property
  # esse é o getter (pegar o atributo)
  def username(self):
    print('estou pegando o atributo')
    return self._username

  @username.setter
  def username(self, new_name):
    print('estou mudando o atributo')
    self._username = new_name

u1 = User()
u1.username = 'outro'
print(u1.username)