import json
from httpApi import bodyValidator, response
from auth import readBearerToken

params = {
    'unidad_productiva_id': ['number'],
    'lote_id': ['number'],
    'periodo_id': ['number'],
    'riegos': ['number'],
    'minutos': ['number'],
    'm3_s_fertilizante': ['number'],
    'm3_c_fertilizante': ['number'],
    'fecha': ['date'],
}

def post(event, context):
    tokenData = readBearerToken(event)
    if not 'username' in tokenData:
        return tokenData

    errors = bodyValidator(event, params)
    if errors is not None:
        return errors

    data = json.loads(event['body'])

    return response({'user': data}, 200)
