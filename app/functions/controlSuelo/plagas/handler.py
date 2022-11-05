import json
from httpApi import bodyValidator, response
from auth import readBearerToken

def post(event, context):
    tokenData = readBearerToken(event)
    if 'message' in tokenData:
        return tokenData

    missingParams = bodyValidator(event, [
        'unidad_productiva_id',
        'lote_id',
        'tunel',
        'surco',
        'plaga_id',
        'conteo',
        'area_invasion',
        'severidad_danio',
        'zona_danio',
        'etapa_medida',
        'aplicaciones',
        'observaciones',
        'temperatura',
        'fecha'
    ])
    if missingParams is not None:
        return missingParams

    data = json.loads(event['body'])

    return response({'user': data}, 200)
