from flask_restx import Resource
from globals import get_connection


# POST /sessions/checkout-all
class CheckoutAll(Resource):

    def post(self):
        '''log off all pilots'''
        connection = get_connection("database_server.db")
        cursor = connection.cursor()

        cursor.execute(
            'UPDATE Flugsession SET Endzeit = datetime() WHERE Endzeit is NULL'
        )

        connection.commit()
        connection.close()

        return {}
