from src import write_in_database


def http_post():
    """
    Has its default params to build data
    and send it to write_in_database() route
    """
    http_message = {
        "http_method": "POST",
        "http_header": {
            "token": "Bearer 3drie44303ifoskj",
            "origin": "http://drydesert.com.br"
        },
        "http_body": {
            "name": "Chester",
            "age": "41"
        }
    }

    write_in_database(http_message)
