EMPTY = '**empty**'

class User:
	def __init__(self, db_obj = None):
		if db_obj:
			self.id = db_obj[0]
			self.login = db_obj[5]
			self.tid = db_obj[1]
			self.tcid = db_obj[2]
			self.created_at = db_obj[3]
			self.is_deleted = db_obj[4]
		else:
			self.id = -1
			self.login = EMPTY
			self.tid = -1
			self.tcid = -1
			self.created_at = ()
			self.is_deleted = False

	def __repr__(self):
		return f'<id={self.id},login={self.login},telegram_id={self.tid},telegram_chat_id={self.tcid}>'

	def export (self):
		return [self.id, self.tid, self.tcid, self.created_at, self.is_deleted, self.login]

	def exportInsert (self):
		return [self.tid, self.tcid, self.is_deleted, self.login]