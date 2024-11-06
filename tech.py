class Tech:
    def __init__(self, name, storage):
        self.name = name
        self.storage = storage

class Phone(Tech):
    def __init__(self, name, storage, color):
        super().__init__(name, storage)
        self.color = color

class Laptop(Tech):
    def __init__(self, name, storage, size):
        super().__init__(name, storage)
        self.size = size