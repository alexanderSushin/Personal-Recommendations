EMPTY = '**empty**'

class User:
	def __init__ (self):
		self.id = -1
		self.login = EMPTY
		self.uid = -1
		self.ratings = []

	def __init__(self, db_obj):
		self.login = db_obj
		self.uid = -1
		self.ratings = []