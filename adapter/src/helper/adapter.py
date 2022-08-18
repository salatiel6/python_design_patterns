class Adapter:
    """
    Has methods to adapt request bodies in alternative formats to the
    project pattern
    """

    @staticmethod
    def adapt_iron_framework(http_request) -> {}:
        """
        Adapts iron framework request body to the project default

        :param http_request: iron framework request body
        :return: adapted http request body
        """

        adapted_http_request = {
            "method": http_request["HTTP_method"],
            "header": {
                "token": http_request["HTTP_header"]["token"],
                "origin": http_request["HTTP_header"]["origin"]
            },
            "body": {
                "name": http_request["HTTP_body"]["name"],
                "age": http_request["HTTP_body"]["age"]
            }
        }

        return adapted_http_request

    @staticmethod
    def adapt_gold_framework(http_request) -> {}:
        """
        Adapts gold framework request body to the project default

        :param http_request: gold framework request body
        :return: adapted http request body
        """

        adapted_http_request = {
            "method": http_request["http_method"],
            "header": {
                "token": http_request["http_header"]["token"],
                "origin": http_request["http_header"]["origin"]
            },
            "body": {
                "name": http_request["http_body"]["name"],
                "age": http_request["http_body"]["age"]
            }
        }

        return adapted_http_request
