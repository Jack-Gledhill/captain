class CustomException(Exception):
    pass


class MissingSubcommand(CustomException):
    pass

class AccessDenied(CustomException):
	pass

class LookupFailed(CustomException):
    def __init__(self, item):
        self.item = item
	
class NotConfigured(CustomException):
	def __init__(self, missing_config):
		self.missing_config = missing_config