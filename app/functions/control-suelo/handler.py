from httpApi import response
from auth import readBearerToken

def post(event, context):
  tokenData = readBearerToken(event)
  if not 'username' in tokenData:
    return tokenData

  return response({ 'user': tokenData }, 200)