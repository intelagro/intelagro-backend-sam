from dataclasses import replace
import json
import os
from httpApi import response
import jwt

SECRET = os.environ['JWT_SECRET']


def createToken(data: dict):
    return jwt.encode(data, SECRET, algorithm="HS256")


def decodeToken(token: str):
    try:
        data = jwt.decode(token, SECRET, algorithms="HS256")
        return data
    except:
        return None


def readBearerToken(event):
    if not 'Authorization' in event['headers']:
        return response({'message': "Bearer token no proporcionado"}, 401)

    token = event['headers']['Authorization'].replace('Bearer ', '')
    data = decodeToken(token)
    if data is None:
        return response({'message': "Token invalido"}, 401)
    
    return data
