from src import write_in_database


def http_post():
    """
    Has its default params to build data
    and send it to write_in_database() route
    """
    http_message = {
        "HTTP_method": "POST",
        "HTTP_header": {
            "token": "Bearer dlfkjw54094j340r",
            "origin": "http://freshwather.com.br"
        },
        "HTTP_body": {
            "name": "Mike",
            "age": "44"
        }
    }

    write_in_database(http_message)
