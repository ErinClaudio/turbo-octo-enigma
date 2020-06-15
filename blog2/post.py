class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    #def__repr__(self):


    def json(self):
        return {
            "title": self.title,
            "content": self.content,
        }
