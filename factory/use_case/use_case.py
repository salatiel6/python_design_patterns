from interface import DatabaseInterface
from typing import Dict, Union


class UseCase:
    def __init__(self, repository: DatabaseInterface):
        self._repository = repository

    def do_something(self, data: bool) -> Union[Dict, None]:
        if data is True:
            repository_response = self._repository.select_one()
            return repository_response

        return None
