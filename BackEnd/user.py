'''
* Usuario (User)
- id (id)
- codigo_empresa (code_business)
- nombre (name)
- nit (nit)
- direccion (address)
- Correo electronico (email)
- nombre de usuario (username)
- contrasena (password)
- tipo_usuario (user_type)
'''

class User:

    def __init__(self, id, code_business, name, nit, address, email, username, password, user_type):
        self.id = id
        self.code_business = code_business
        self.name = name
        self.nit = nit
        self.address = address
        self.email = email
        self.username = username
        self.password = password
        self.user_type = user_type

    # Metodos GET y SET
    # id
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    # code_business
    def getCode_business(self):
        return self.code_business
    
    def setCode_business(self, code_business):
        self.code_business = code_business

    # name
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    # nit
    def getNit(self):
        return self.nit
    
    def setNit(self, nit):
        self.nit = nit
    
    # address
    def getAddress(self):
        return self.address
    
    def setAddress(self, address):
        self.address = address

    # email
    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    # username
    def getUsername(self):
        return self.username
    
    def setUsername(self, username):
        self.username = username

    # password
    def getPassword(self):
        return self.password
    
    def setPassword(self, password):
        self.password = password

    # user_type
    def getUser_type(self):
        return self.user_type
    
    def setUser_type(self, user_type):
        self.user_type = user_type