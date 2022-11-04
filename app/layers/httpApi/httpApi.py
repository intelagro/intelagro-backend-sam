import json

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

def bodyValidator(body, params: list) -> any or None:
    if type(body) is not str:
        return response({
            'message': 'Faltan parametros en la peticion',
            'params': params
        }, 400)
    missingParams = []

    data = json.loads(body)
    for param in params:
        if not param in data:
            missingParams.append(param)

    if len(missingParams) != 0:
        return response({
            'message': 'Faltan parametros en la peticion',
            'params': missingParams
        }, 400)
    return None