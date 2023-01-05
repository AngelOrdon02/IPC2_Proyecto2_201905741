'''
* Empresa (Business)
- id (id)
- codigon (code)
- nombre (name)
'''

class Business:

    def __init__(self, id, code, name):
        self.id = id
        self.code = code
        self.name = name
    
    # Metodos GET y SET
    # id
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    # code
    def getCode(self):
        return self.code
    
    def setCode(self, code):
        self.code = code

    # name
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name