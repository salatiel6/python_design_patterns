import config_path # noqa

from factory import MysqlFactory, PostgresFactory

use_case = MysqlFactory.create()
response = use_case.do_something(True)
print(response)

use_case = PostgresFactory.create()
response = use_case.do_something(True)
print(response)
