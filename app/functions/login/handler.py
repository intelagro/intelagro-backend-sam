from cats import catPlagas, catUnidadesProductivas
from httpApi import response, validateData
import json
from auth import createToken
from db import Database


params = {
        'username': ['string'],
        'password': ['string'],
    }



def login(event, context):
    errors = validateData(event, params)
    if errors is not None:
        return errors

    data = json.loads(event['body'])
    username = data['username']
    password = data['password']

    user = Database.query(
        f'SELECT * FROM cat_usuarios WHERE usuario = "{username}"')

    if len(user) == 0 or user[0]['pass'] != password:
        return response({
            'message': 'Las credenciales son incorrectas'
        }, 404)

    user = user[0]

    if user['session_v2'] == 1 and user['tipo'] == 'usuario':
        return response({
            'message': 'Sesion iniciada en otro dispositivo'
        }, 403)

    tokenData = {
        'id': user['cat_usuarios_id'],
        'username': user['usuario'],
        'capturista': user['capturista']
    }

    token = createToken(tokenData)

    id = user['cat_usuarios_id']
    Database.query(
        f'UPDATE cat_usuarios SET session_v2 = 1 WHERE cat_usuarios_id = {id}')

    # CATALOGOS
    unidades_productivas = catUnidadesProductivas(
        user['cat_usuarios_licencias_id'])
    plagas = catPlagas(user['cat_usuarios_licencias_id'])

    return response(
        {
            'username': user['usuario'],
            'name': user['nombre'],
            'token': token,
            'cats': {
                'unidades_productivas': unidades_productivas,
                'control_suelo': {
                    'plagas': plagas
                }
            }

        }, 200)
