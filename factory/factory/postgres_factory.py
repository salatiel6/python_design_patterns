from use_case import UseCase
from databases import PostgresRepository


class PostgresFactory:
    @staticmethod
    def create() -> UseCase:
        return UseCase(PostgresRepository())
