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
