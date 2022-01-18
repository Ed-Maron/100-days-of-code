class City:

    def __init__(self, name):
        self.__name = name
        self.__id = None
    
    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if  id == -1:
            self.__id = 0
        else:
            self.__id = id