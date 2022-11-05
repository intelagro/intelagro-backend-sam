import json
from httpApi import response, validateData
from auth import readBearerToken

params = {
    'unidad_productiva_id': ['number'],
    'lote_id': ['number'],
    'tunel': ['number'],
    'surco': ['number'],
    'plaga_id': ['number'],
    'conteo': ['number'],
    'area_invasion': ['string'],
    'severidad_danio': ['string'],
    'zona_danio': ['string'],
    'etapa_medida': ['string'],
    'aplicaciones': ['string'],
    'observaciones': ['string'],
    'temperatura': ['number'],
    'fecha': ['date'],
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
