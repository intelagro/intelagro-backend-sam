import json
from httpApi import response, validateData
from auth import readBearerToken
from db import Database

params = {
    'unidad_productiva_id': ['number'],
    'lote_id': ['number'],
    'surco': ['number'],
    'maceta': ['number'],
    'ph': ['number'],
    'ce': ['number'],
    'na': ['number'],
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

    Database.insert(table='tr_control_de_suelo_phcena_app', data={
        'cat_holding_03_empresas_unidades_productivas_id': data['unidad_productiva_id'],
        'cat_holding_04_unidades_productivas_lotes_id': data['lote_id'],
        'surco': data['surco'],
        'maceta': data['maceta'],
        'ph': data['ph'],
        'ce': data['ce'],
        'na': data['na'],
        'fecha_de_captura': data['fecha'],
        'capturista': tokenData['capturista']
    })

    return response({
        'message': 'Se ha agregado el registro'
    }, 200)
