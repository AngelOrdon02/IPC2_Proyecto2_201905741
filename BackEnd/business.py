'''
* Empresa (Business)
- id (id)
- nombre (name)
'''

class Business:

    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    # Metodos GET y SET
    # id
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    # name
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name