from use_case import UseCase
from databases import MysqlRepository


class MysqlFactory:
    @staticmethod
    def create() -> UseCase:
        return UseCase(MysqlRepository())
