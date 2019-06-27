class Sport(object):
    def __init__(self, name, time, type, filename):
        self.name = name
        self.time = time
        self.type = type
        self.filename = filename
        assert type in ["team", "pair"], "bad type of sport " + name
