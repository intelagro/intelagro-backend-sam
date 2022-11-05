import os
import mysql.connector as mysql
import json

class Database:
    connection = mysql.connect(
        host = os.environ['DB_HOST'],
        username = os.environ['DB_USERNAME'],
        password = os.environ['DB_PASSWORD'],
        database = os.environ['DB_NAME']
    )


    @staticmethod
    def query(query: str):
        db_cursor = Database.connection.cursor(dictionary=True)
        db_cursor.execute(query)
        result = json.dumps(db_cursor.fetchall(), default=str)
        return json.loads(result)

    @staticmethod
    def insert(table: str, data: dict):
        keys = data.keys()
        keys_str = ''
        for key in keys:
            keys_str += f'{key}, '
        keys_str = keys_str[0:len(keys_str)-2]        

        values_str = ''
        values = data.values()
        for value in values:
            if type(value) is str:
                values_str += f'"{value}", '
            else:
                values_str += f'{value}, '
        values_str = values_str[0:len(values_str)-2]

        query = f'INSERT INTO {table} ({keys_str}) VALUES ({values_str});'
        Database.query(query)
