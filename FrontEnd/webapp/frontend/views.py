from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

import json

from django.contrib import messages
import xml.etree.ElementTree as ET
import datetime

# Home
def home(request):
    return render(request, "homeView.html", {})

# Login
def login_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if (username != None and password != None):
            params = {'username': username, 'password': password}
            response = requests.post('http://127.0.0.1:3000/login', json = params)
            
            res = response.json()

            if (res['state'] == 1):
                request.session['session_id'] = str(res['id'])
                request.session['session_username'] = str(username)
                return redirect('users')
            elif (res['state'] == 2):
                messages.info(request, 'Contraseña incorrecta')
                return render(request, "auth/loginView.html", {})
            elif (res['state'] == 3):
                messages.info(request, 'Nombre de usuario incorrecto')
                return render(request, "auth/loginView.html", {})
            elif (res['state'] == 4):
                messages.info(request, 'Nombre de usuario y contraseña incorrectos')
                return render(request, "auth/loginView.html", {})

    return render(request, "auth/loginView.html", {})

# --------------- Administration ---------------

# Metodo para la vista userView.html
def users(request):

    response = requests.get('http://127.0.0.1:3000/users')

    users = response.json()

    return render(request, "administration/usersView.html", {'users': users['users']})

# Create user
def add_user(request):
    
    if request.method == 'POST':
        id = request.POST.get('id', None)
        name = request.POST.get('name', None)
        nit = request.POST.get('nit', None)
        address = request.POST.get('address', None)
        email = request.POST.get('email', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user_type = 1

        params = {
            'id': id,
            'name': name,
            'nit': nit,
            'address': address,
            'email': email,
            'username': username,
            'password': password,
            'user_type': user_type
            }
        response = requests.post('http://127.0.0.1:3000/users', json = params)
        
        res = response.json()

        return redirect('users')

    return render(request, "administration/userNewView.html", {})

# Metodo para la vista settingView.html
def setting(request):
    return render(request, "administration/settingView.html", {})

# Metodo para la vista resourcesView.html
def resources(request):

    response = requests.get('http://127.0.0.1:3000/resources')

    #convert reponse data into json
    resources = response.json()

    return render(request, "administration/resourcesView.html", {'resources': resources['resources']})

# Create resource
def add_resource(request):
    
    if request.method == 'POST':
        id = request.POST.get('id', None)
        name = request.POST.get('name', None)
        abbreviation = request.POST.get('abbreviation', None)
        metrics = request.POST.get('metrics', None)
        type = request.POST.get('type', None)
        worth = request.POST.get('worth', None)
        id_config = request.POST.get('id_config', None)

        params = {
            'id': id,
            'name': name,
            'abbreviation': abbreviation,
            'metrics': metrics,
            'type': type,
            'worth': worth,
            'id_config': id_config
            }
        response = requests.post('http://127.0.0.1:3000/resources', json = params)
        return redirect('resources')

    return render(request, "administration/resourceNewView.html", {})

# Metodo para la vista categoriesView.html
def categories(request):

    response = requests.get('http://127.0.0.1:3000/categories')

    #convert reponse data into json
    categories = response.json()

    return render(request, "administration/categoriesView.html", {'categories': categories['categories']})

# Create category
def add_category(request):
    
    if request.method == 'POST':
        id = request.POST.get('id', None)
        name = request.POST.get('name', None)
        description = request.POST.get('description', None)
        load = request.POST.get('load', None)

        params = {
            'id': id,
            'name': name,
            'description': description,
            'load': load
            }
        response = requests.post('http://127.0.0.1:3000/categories', json = params)
        return redirect('categories')

    return render(request, "administration/categoryNewView.html", {})

# Metodo para la vista settingsView.html
def settings(request):

    response = requests.get('http://127.0.0.1:3000/settings')

    #convert reponse data into json
    settings = response.json()

    return render(request, "administration/settingsView.html", {'settings': settings['settings']})

# Create setting
def add_setting(request):
    
    if request.method == 'POST':
        id = request.POST.get('id', None)
        name = request.POST.get('name', None)
        description = request.POST.get('description', None)
        dimensional = request.POST.get('dimensional', None)
        cost = request.POST.get('cost', None)
        id_category = request.POST.get('id_category', None)

        params = {
            'id': id,
            'name': name,
            'description': description,
            'dimensional': dimensional,
            'cost': cost,
            'id_category': id_category
            }
        response = requests.post('http://127.0.0.1:3000/settings', json = params)
        return redirect('settings')

    return render(request, "administration/settingNewView.html", {})

# Metodo para la vista instancesView.html
def instances(request):

    response = requests.get('http://127.0.0.1:3000/instances')

    #convert reponse data into json
    instances = response.json()

    return render(request, "administration/instancesView.html", {'instances': instances['instances']})

# Create instance
def add_instance(request):
    
    if request.method == 'POST':
        id = request.POST.get('id', None)
        name = request.POST.get('name', None)
        condition = request.POST.get('condition', None)
        start = request.POST.get('start', None)
        end = request.POST.get('end', None)
        id_config = request.POST.get('id_config', None)
        id_user = request.POST.get('id_user', None)

        # start_str = datetime.datetime.strptime(str(start), '%Y/%m/%d').strftime('%Y/%m/%d')
        # end_str = end.datetime.strftime("%d/%m/%Y")

        params = {
            'id': id,
            'name': name,
            'condition': condition,
            'start': start,
            'end': end,
            'id_config': id_config,
            'id_user': id_user
            }
        response = requests.post('http://127.0.0.1:3000/instances', json = params)
        return redirect('instances')

    return render(request, "administration/instanceNewView.html", {})

# Metodo para la vista helpView.html
def help(request):
    return render(request, "administration/helpView.html", {})