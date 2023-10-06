class Makeup():

    def __init__(self, brand, type):
        self._brand = brand
        self._type = type

        # TODO: add people who bought makeup item
        # TODO: add purchases of makeup item
        self.owners = []
        self.purchases = []

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if not hasattr(self, "brand"):
            self._brand = brand
        else:
            raise Exception("Brand can be set only once!")
        
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        if type(type) == str:
            self._type = type
        else:
            raise Exception("Type must be a string!")
        
    def __repr__(self):
        return f"Brand: {self.brand}\nMakeup Type: {self.type}"