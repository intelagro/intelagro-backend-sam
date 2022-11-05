from httpApi import response, bodyValidator
import json
from auth import decodeToken
from db import Database


def logout(event, context):
    missingParams = bodyValidator(event, ['token'])
    if missingParams is not None:
        return missingParams

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
