from .controller import db_write


class Process:

    @staticmethod
    def write_in_database(http_request):
        """
        Receives the http_request, checks in the body if the token is valid,
        and calls db_write() method to save the data.

        :param http_request: body from the request
        """

        token = http_request['header']['token']

        if token:
            print("Token Authentified")

            name = http_request['body']['name']
            age = http_request['body']['age']
            db_write(name, age)
