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
        'periodo_id',
        'fecha',
        'riegos',
        'minutos',
        'm3_s_fertilizante',
        'm3_c_fertilizante'
    ])
    if missingParams is not None:
        return missingParams

    data = json.loads(event['body'])

    return response({'user': data}, 200)
