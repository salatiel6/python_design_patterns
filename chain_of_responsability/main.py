import config_path # noqa

from validation import Validation

fruit_validation = Validation("fruit")
fruit_validation.process()

meat_validation = Validation("meat")
meat_validation.process()
