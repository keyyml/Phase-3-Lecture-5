class People():

    def __init__(self, name, age):
        self._name = name
        self._age = age

        # TODO: add makeup items purchased by person
        # TODO: add purchases by person
        self.makeup_items = []
        self.purchases = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and len(name) > 3:
            self._name = name
        else:
            raise Exception("Name must be a string of more than 3 characters!")
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if type(age) == int and age > 12:
            self._age = age
        else:
            raise Exception("Age must be an integer greater than 12!")
        
    def __repr__(self):
        return f"\nName: {self.name}\nAge: {self.age}"