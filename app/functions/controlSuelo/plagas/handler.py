import json
from httpApi import response, validateData
from auth import readBearerToken
from db import Database

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

    Database.insert(table = 'tr_control_de_plagas_app', data = {
        'cat_holding_03_empresas_unidades_productivas_id': data['unidad_productiva_id'],
        'cat_holding_04_unidades_productivas_lotes_id': data['lote_id'],
        'tunel': data['tunel'],
        'surco': data['surco'],
        'cat_control_plagas_y_enfermedades_id': data['plaga_id'],
        'area_de_invasion': data['area_invasion'],
        'conteo': data['conteo'],
        'severidad_de_dano': data['severidad_danio'],
        'zona_danada': data['zona_danio'],
        'etapa_de_medida': data['etapa_medida'],
        'aplicaciones': data['aplicaciones'],
        'observaciones': data['observaciones'],
        'fecha_de_captura': data['fecha'],
        'capturista': tokenData['capturista']
    })

    return response({
        'message': 'Se ha agregado el registro'
    }, 200)

