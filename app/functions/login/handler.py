from httpApi import response, bodyValidator
import json
from auth import createToken
from db import Database


def login(event, context):
    missingParams = bodyValidator(event['body'], ['username', 'password'])
    if missingParams is not None:
        return missingParams

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

    print(user)
    if user['session_v2'] == 1 and user['tipo'] == 'usuario':
        return response({
            'message': 'Sesion iniciada en otro dispositivo'
        }, 403)

    tokenData = {
        'id': user['cat_usuarios_id'],
        'username': user['usuario']
    }

    token = createToken(tokenData)

    id = user['cat_usuarios_id']
    Database.query(
        f'UPDATE cat_usuarios SET session_v2 = 1 WHERE cat_usuarios_id = {id}')

    return response(
        {
            'username': user['usuario'],
            'name': user['nombre'],
            'token': token

        }, 200)