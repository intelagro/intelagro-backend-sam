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
        'surco',
        'maceta',
        'ph',
        'ce',
        'na',
        'fecha'
    ])
    if missingParams is not None:
        return missingParams

    data = json.loads(event['body'])

    return response({'user': data}, 200)
