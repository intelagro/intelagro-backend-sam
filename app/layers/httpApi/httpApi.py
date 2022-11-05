import json
import re

def response(body: dict, status: int):
    return {
        'headers': {
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Accept": "*/*",
            "Content-Type": "application/json"
        },
        "statusCode": status,
        "body": json.dumps(body)
    }


def validateData(event, params: dict) -> any or None:

    data = {}
    if type(event['body']) is str:
        data = json.loads(event['body'])
    errors = []

    for key, value in params.items():
        # Comprobar si el parametro fue enviado
        if not key in data:
            if key != 'options':
                error = {
                    'param': key,
                    'error': 'Campo no enviado'
                }
                errors.append(error)
            continue

        for validator in value:
            currentValue = data[key]

            # String
            if validator == 'string':
                if type(currentValue) is not str:
                    error = {
                        'param': key,
                        'error': 'Debe ser de tipo string'
                        }
                    errors.append(error)
                    continue

            # Number
            if validator == 'number':
                if type(currentValue) is not int:
                    error = {
                        'param': key,
                        'error': 'Debe ser de tipo numerico'
                        }
                    errors.append(error)
                    continue
            # Range
            if validator == 'range':
                min = params['options'][f'{key}_min']
                max = params['options'][f'{key}_max']
                if type(currentValue) is not int or currentValue < min or currentValue > max:
                    error = {
                        'param': key,
                        'error': f'Debe ser mayor a {min} y menor que {max}'
                        }
                    errors.append(error)
                    continue

            # Length
            if validator == 'length':
                min = params['options'][f'{key}_min']
                max = params['options'][f'{key}_max']
                if type(currentValue) is not str or len(currentValue) < min or len(currentValue) > max:
                    error = {
                        'param': key,
                        'error': f'Debe tener entre {min} y {max} caracteres'
                        }
                    errors.append(error)
                    continue

            if validator == 'date':
                if type(currentValue) is not str or re.fullmatch('^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$', currentValue) is None:
                    error = {
                        'param': key,
                        'error': f'El formato debe ser YYYY-MM-DD'
                        }
                    errors.append(error)
                    continue

    if len(errors) != 0:
        return response({
            'message': 'Hay errores en los parametros enviados',
            'errors': errors
        }, 400)
