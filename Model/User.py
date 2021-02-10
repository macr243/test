class User:

    def __init__(self, id=None, name=None, email=None):
        if id is None:
            id = 1
        self.id = id
        self.name = name
        self.email = email
