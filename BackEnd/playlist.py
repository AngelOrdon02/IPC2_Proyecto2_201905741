'''
* Lista de reproduccion (playlist)
- id (id)
- id_usuario (id_user)
- id_categoria (id_category)
- nit_cliente (nit_user)
- vinyl (vinyl)
- compacto (compact)
'''

class Playlist:
    
    def __init__(self, id, id_user, id_category, nit_user, vinyl, compact):
        self.id = id
        self.id_user = id_user
        self.id_category = id_category
        self.nit_user = nit_user
        self.vinyl = vinyl
        self.compact = compact

    # Metodos GET y SET
    # id
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    # id_user
    def getId_user(self):
        return self.id_user
    
    def setId_user(self, id_user):
        self.id_user = id_user
    
    # id_category
    def getId_category(self):
        return self.id_category

    def setId_category(self, id_category):
        self.id_category = id_category
    
    # nit_user
    def getNit_user(self):
        return self.nit_user

    def setNit_user(self, nit_user):
        self.nit_user = nit_user

    # vinyl
    def getVinyl(self):
        return self.vinyl
    
    def setVinyl(self, vinyl):
        self.vinyl = vinyl

    # compact
    def getCompact(self):
        return self.compact

    def setCompact(self, compact):
        self.compact = compact