'''
* Cancion (Song)
- id (id)
- nombre (name)
- año (year)
- artista (artist)
- genero (gender)
'''

class Song:

    def __init__(self, id, name, year, artist, gender):
        self.id = id
        self.name = name
        self.year = year
        self.artist = artist
        self.gender = gender
    
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

    # year
    def getYear(self):
        return self.year
    
    def setYear(self, year):
        self.year = year
    
    # artist
    def getArtist(self):
        return self.artist
    
    def setArtist(self, artist):
        self.artist = artist

    # gender
    def getGender(self):
        return self.gender
    
    def setGender(self, gender):
        self.gender = gender