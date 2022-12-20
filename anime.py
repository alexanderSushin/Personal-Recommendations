EMPTY = '**empty**'

class Anime:
	def __init__(self, db_obj=None):
		if not db_obj:
			self.id = -1
			self.shikimory_id = -1
			self.name = EMPTY
			self.russian = EMPTY
			self.url = EMPTY
			self.status = EMPTY
			self.score = -1
			self.episodes = -1
			self.year = -1
			self.rating = EMPTY
			self.description = EMPTY
			self.image_url = EMPTY
			self.genres = []
		else:
			self.id = db_obj[0]
			self.shikimory_id = db_obj[1]
			self.name = db_obj[2]
			self.russian = db_obj[3]
			self.url = db_obj[4]
			self.status = db_obj[5]
			self.score = db_obj[6]
			self.episodes = db_obj[7]
			self.year = db_obj[8]
			self.rating = db_obj[9]
			self.description = db_obj[10]
			self.image_url = db_obj[11]
			self.genres = db_obj[12]

	def __repr__(self):
		return f'<id={self.id},shikimory_id={self.shikimory_id},name={self.name},russian={self.russian},url={self.url},status={self.status},score={self.score}>'

	def export(self):
		return [self.id, self.shikimory_id, self.name, self.russian, self.url, self.status, self.score,self.episodes,self.year,self.rating,self.description,self.image_url,self.genres]

	def exportInsert(self):
		return [self.shikimory_id, self.name, self.russian, self.url, self.status, self.score, self.episodes, self.year, self.rating, self.description, self.image_url, self.genres]