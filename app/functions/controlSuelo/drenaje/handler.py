import json
from httpApi import response, validateData
from auth import readBearerToken

params = {
    'unidad_productiva_id': ['number'],
    'lote_id': ['number'],
    'periodo_id': ['number'],
    'ph_entrada': ['number'],
    'ph_salida': ['number'],
    'ce_entrada': ['number'],
    'ce_salida': ['number'],
    'agua_entrada': ['number'],
    'agua_salida': ['number'],
    'temperatura': ['number'],
    'fecha': ['date']
}


def post(event, context):
    tokenData = readBearerToken(event)
    if not 'username' in tokenData:
        return tokenData

    errors = validateData(event, params)
    if errors is not None:
        return errors

    data = json.loads(event['body'])

    return response({'user': data}, 200)
