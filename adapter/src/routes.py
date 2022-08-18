from .process import Process
from .helper import Adapter


def write_in_database(http_request):
    """
    Instaciate the adpter and the process for making the insertion
    in the database
    """

    adapter = Adapter()
    process = Process()

    # Selects which adaptor to use, based on which framework that
    # is beeing used
    adapted_http_request = adapter.adapt_iron_framework(http_request)

    process.write_in_database(adapted_http_request)
