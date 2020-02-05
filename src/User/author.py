def createAuthorFromMessage(msg):
    return Author(msg.id,msg.name)

class Author():
    def __init__(self,id,name):
        self.id = id
        self.name = name
