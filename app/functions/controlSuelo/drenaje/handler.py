import json
from httpApi import response, validateData
from auth import readBearerToken
from db import Database

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

    Database.insert(table='tr_control_de_suelo_phcet_drenaje_app', data={
        'cat_holding_03_empresas_unidades_productivas_id': data['unidad_productiva_id'],
        'cat_holding_04_unidades_productivas_lotes_id': data['lote_id'],
        'ph_entrada': data['ph_entrada'],
        'ph_salida': data['ph_salida'],
        'ce_entrada': data['ce_entrada'],
        'ce_salida': data['ce_salida'],
        'agua_entrada': data['agua_entrada'],
        'agua_salida': data['agua_salida'],
        'temperatura': data['temperatura'],
        'fecha_de_captura': data['fecha'],
        'capturista': tokenData['capturista']
    })

    return response({
        'message': 'Se ha agregado el registro'
    }, 200)