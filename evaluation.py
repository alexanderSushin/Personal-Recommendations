EMPTY = '**empty**'

class Evaluation:
    def __init__ (self, db_obj = None):
        if db_obj:
            self.user_id = db_obj[0]
            self.anime_id = db_obj[1]
            self.score = db_obj[2]
            self.created_at = db_obj[3]
        else:
            self.user_id = -1
            self.anime_id = -1
            self.score = -1
            self.created_at = ()
    
    def export (self):
        return [self.user_id, self.anime_id, self.score, self.created_at]

    def exportInsert (self):
        return [self.user_id, self.anime_id, self.score]
