EMPTY = '**empty**'

class Genre:
    def __init__ (self, db_obj = False):
        if db_obj:
            self.id = db_obj[0]
            self.name = db_obj[1]
            self.russian = db_obj[2]
            self.kind = db_obj[3]
        else:
            self.id = -1
            self.name = EMPTY
            self.russian = EMPTY
            self.kind = EMPTY
    
    def export (self):
        return [self.id, self.name, self.russian, self.kind]
    
    def exportInsert(self):
        return [self.name, self.russian, self.kind]