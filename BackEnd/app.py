# Importando librerias
from flask import Flask, jsonify, request
from flask_cors import CORS

# from tkinter.tix import Tree
from xml.etree import ElementTree as ET

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

Business_array.append(Business(1, 'A001', "AGOC"))

Playlists.append(Playlist(1, 55555, 'Salsa', 55555, 100, 50))

Songs.append(Song(1, 'Plein De Bisous', 2018, 'Lewis OfMan y Milena Leblanc', 'Dance/Electronica', 15))

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
            'code': business_i.getCode(),
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
        request.json['code'],
        request.json['name']
    )
    Business_array.append(new)
    answer = jsonify({'message': 'Added business'})

    return (answer)

# --------------- Playlist ---------------

# Get playlists
@app.route('/playlists', methods=['GET'])
def selectAllPlaylists():
    global Playlists
    Data = []

    for playlist in Playlists:
        Fact = {
            'id': playlist.getId(),
            'nit_user': playlist.getNit_user(),
            'id_category': playlist.getId_category(),
            'vinyl': playlist.getVinyl(),
            'compact': playlist.getCompact()
        }
        Data.append(Fact)
    
    answer = jsonify({'playlists': Data})

    return (answer)

# --------------- Song ---------------

# Get songs
@app.route('/songs', methods=['GET'])
def selectAllSongs():
    global Songs
    Data = []

    for song in Songs:
        Fact = {
            'id': song.getId(),
            'name': song.getName(),
            'year': song.getYear(),
            'artist': song.getArtist(),
            'gender': song.getGender(),
            'cost': song.getCost()
        }
        Data.append(Fact)
    
    #answer = jsonify(Data)
    answer = jsonify({'songs': Data})

    return (answer)

# --------------- Carga Masiva ---------------

# msg_config
@app.route('/msg_config', methods=['POST'])
def msg_config():
    global Users
    global Business_array
    global Playlists
    global Songs

    # Contadores para answer
    cont_playlists = 0
    cont_users = 0
    cont_business = 0
    
    # Codigo
    # data = request.json()
    data_answer = request.json['data']
    
    if (data_answer == ''):
        answer = jsonify({'status': '400', 'message': 'None data'})
    else:
        # xml = data_answer.data.decode('utf-8')
        # raiz = ET.XML(data_answer)
        # for elemento in raiz:
        #     # (elemento.attrib['name'],elemento.attrib['artist'],elemento.attrib['image'],elemento.text)
        #     pass
        #     print("-> ", elemento.attrib['id'])

        root = ET.XML(data_answer)

        playlist_clients = root[0]

        clients_data = root[1]

        business_data = root[2]

        
        for r in playlist_clients:

            # Playlist
            nit_xml = r[0]
            vinyl_xml = r[1]
            compact_xml = r[2]
            category_xml = r[3]

            playlist_one = Playlists[-1]
            position = playlist_one.getId() + 1

            new_playlist = Playlist(
                # request.json['id'],
                position,
                nit_xml.text,
                category_xml.text,
                nit_xml.text,
                vinyl_xml.tail,
                compact_xml.tail
                # vinyl_xml.text,
                # compact_xml.text
            )
            Playlists.append(new_playlist)
            cont_playlists += 1 # Contador

            # Canciones
            songs_data = r.text.replace('\n', '')
            songs_data = r[4]
            
            for song in songs_data:
                name_song = song[0]
                year_song = song[1]
                artist_song = song[2]
                gender_song = song[3]

                cost = song[1].tail.replace('\n', '')

                # Add song in list Songs[]
                # print("song name: ", str(name_song.text))
                # print("song name: ", str(year_song.text))
                # print("song name: ", str(artist_song.text))
                # print("song name: ", str(gender_song.text))

                song_one = Songs[-1]
                position = song_one.getId() + 1

                new_song = Song(
                    # request.json['id'],
                    position,
                    name_song.text,
                    year_song.text,
                    artist_song.text,
                    gender_song.text,
                    cost.strip()
                )
                Songs.append(new_song)

            # print("var: ", str(nit_xml.text))
        
        for r in clients_data:
            nit_client = r.attrib['nit']
            name_client = r[0]
            username_client = r[1]
            password_client = r[2]
            address_client = r[3]
            email_client = r[4]
            user_type_client = 2 # Usuario normal


            # print("var: ", str(nit_client))
            # print("var: ", str(name_client.text))

            # global Users

            # obteniendo el ultimo id para tener un correlativo
            user = Users[-1]
            position = user.getId() + 1

            new = User(
                # request.json['id'],
                position,
                name_client.text,
                nit_client,
                address_client.text,
                email_client.text,
                username_client.text,
                password_client.text,
                user_type_client
            )
            Users.append(new)
            cont_users += 1 # contador

            # Users.append(User(position, name_client, nit_client, address_client, email_client, username_client, password_client, user_type_client))
        
        for r in business_data:
            code_business = r.attrib['id']
            name_business = r[0]

            # obteniendo el ultimo id para tener un correlativo
            business_one = Business_array[-1]
            position = business_one.getId() + 1

            new = Business(
                # request.json['id'],
                position,
                code_business,
                name_business.text
            )
            Business_array.append(new)
            cont_business += 1 # contador

        # for r in root:
        #     variable = r[0][0]
        #     print("var: ", str(variable.text))

        # answer = jsonify({'message': data_answer}),200
        answer = jsonify({'status': '200', 'playlists': cont_playlists, 'users': cont_users, 'business': cont_business})
    return (answer)

# --------------- FIN RUTAS ---------------

# Para que se ejecute el API
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)