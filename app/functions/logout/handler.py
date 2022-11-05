from httpApi import response, validateData
import json
from auth import decodeToken
from db import Database

params = {
    'token': ['string']
}


def logout(event, context):
    errors = validateData(event, params)
    if errors is not None:
        return errors

    data = json.loads(event['body'])

    tokenData = decodeToken(data['token'])

    if tokenData is None:
        return response({
            'message': 'Token invalido'
        }, 400)

    id = tokenData["id"]
    Database.query(f'UPDATE cat_usuarios SET session_v2 = 0 WHERE cat_usuarios_id={id}')

    return response({
        'message': 'Sesion cerrada'
    }, 200)
