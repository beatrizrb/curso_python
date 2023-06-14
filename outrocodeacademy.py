class School:
    def __init__(self, name, level, value):
    #print('ate aqui tudo bem')
        self._name = name
        self._noS = value
        self._level = level
    
    def name(self):
        return self._name

    
    def level(self):
        return self._level

    @property 
    def noS(self):
        return self._noS
    
    @noS.setter
    def noS(self, outro):
        print('Estou mudando')
        self._noS = outro
    
    def __repr__(self):
        # toda vez que eu printar o objeto aparece o abaixo
        return(f'A {self._level} school named {self._name} with {self._noS} students')


a1 = School('oi', 'primario', 1000)
#print(a1.noS)
print(a1)
print(repr(a1))
#a1.noS = 20000
#print(a1.noS)
#print(repr(a1))