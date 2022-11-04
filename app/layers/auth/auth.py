import os
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