# Importando librerias
from flask import Flask, jsonify, request
from flask_cors import CORS

import json

# Importando modelos
from user import User
from song import Song
from playlist import Playlist
from playlist_song import Playlist_song
from business import Business
from category import Category

app = Flask(__name__)

CORS(app)

# Declaracion de objetos
Users = []
Songs = []
Playlists = []
Playlist_song_array = []
Business_array = []
Category = []

# Datos ingresados
Users.append(User(1, 'Angel Ordon', 55555, 'Zona 18', 'angel@email.com', 'root', 'root', 1))

Business_array.append(Business(1, "AGOC"))

# --------------- INICIO RUTAS ---------------

@app.route('/', methods=['GET'])
def rutaInicial():
    #global cont_song
    return ("Corriendo API :D, Hola mundo!")

# --------------- Auth ---------------

@app.route('/login', methods=['POST'])
def loginUser():
    global Users

    '''
    Si el state = 0 significa que hubo un error
    codigo cero (0) error
    Si el state = 1 significa que si se loggeo con exito
    codigo uno (1) username y password correctos
    Si el state = 2 significa que el password esta incorrecta
    codigo dos (2) username correcto y password incorrecto
    Si el state = 3 significa que el usuario esta incorrecto
    codigo tres (3) username incorrecto y password correcto
    Si el state = 4 significa que los datos son incorrectos
    codigo cuatro (4) username y password incorrectos
    '''

    username = request.json['username']
    password = request.json['password']
    id_user = 0

    state_username = False
    state_password = False
    state = 0

    for i in range(len(Users)):
        if username == Users[i].getUsername():
            state_username = True
            id_user = Users[i].getId()
            break
    
    for i in range(len(Users)):
        if password == Users[i].getPassword():
            state_password = True
            break
    
    if (state_username == False) and (state_password == False):
        state = 4
    elif (state_username == False) and (state_password == True):
        state = 3
    elif (state_username == True) and (state_password == False):
        state = 2
    elif (state_username == True) and (state_password == True):
        state = 1

    answer = jsonify({'message': 'Login process', 'state': state, 'id': id_user})
    return (answer)
    #answer = jsonify({'message': 'Added user'})
    #return (answer)


# --------------- User ---------------

# Get users
@app.route('/users', methods=['GET'])
def selectAllUsers():
    global Users
    Data = []

    for user in Users:
        Fact = {
            'id': user.getId(),
            'name': user.getName(),
            'nit': user.getNit(),
            'address': user.getAddress(),
            'email': user.getEmail(),
            'username': user.getUsername(),
            'password': user.getPassword(),
            'user_type': user.getUser_type()
        }
        Data.append(Fact)
    
    answer = jsonify({'users': Data})
    #answer = jsonify(Data)

    return (answer)

# Post user
@app.route('/users', methods=['POST'])
def insertUser():
    global Users

    # obteniendo el ultimo id para tener un correlativo
    user = Users[-1]
    position = user.getId() + 1

    new = User(
        # request.json['id'],
        position,
        request.json['name'],
        request.json['nit'],
        request.json['address'],
        request.json['email'],
        request.json['username'],
        request.json['password'],
        request.json['user_type']
    )
    Users.append(new)
    answer = jsonify({'message': 'Added user'})

    return (answer)

# --------------- Business ---------------

# Get business
@app.route('/business', methods=['GET'])
def selectAllBusiness():
    global Business_array
    Data = []

    for business_i in Business_array:
        Fact = {
            'id': business_i.getId(),
            'name': business_i.getName()
        }
        Data.append(Fact)
    
    answer = jsonify({'business': Data})
    #answer = jsonify(Data)

    return (answer)

# Post business
@app.route('/business', methods=['POST'])
def insertBusiness():
    global Business_array

    # obteniendo el ultimo id para tener un correlativo
    business_one = Business_array[-1]
    position = business_one.getId() + 1

    new = Business(
        # request.json['id'],
        position,
        request.json['name']
    )
    Business_array.append(new)
    answer = jsonify({'message': 'Added business'})

    return (answer)

# --------------- FIN RUTAS ---------------

# Para que se ejecute el API
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)