class Purchase():

    # TODO: make list of all purchases
    all = []

    def __init__(self, person, makeup_item, date = "03/03/2020"):
        self._person = person
        self._makeup_item = makeup_item
        self._date = date

        Purchase.all.append(self)

        # TODO: construct purchase object as SSOT
        person.makeup_items.append(makeup_item)
        person.purchases.append(self)
        makeup_item.owners.append(person)
        makeup_item.purchases.append(self)

    # TODO: make property for person (must be instance of People class
    # TODO: make property for makeup_item (must be instance of Makeup class)
    @property 
    def person(self):
        return self._person
    @person.setter
    def person(self, person):
        from People import People
        if isinstance(person, People):
            self._person = person
        else: 
            raise Exception("Person must be an instance of people class!")
    
    @property 
    def makeup_item(self):
        return self._makeup_item
    @makeup_item.setter
    def makeup_item(self, makeup_item):
        from Makeup import Makeup
        if isinstance(makeup_item, Makeup):
            self._makeup_item = makeup_item
        else: 
            raise Exception("Makeup item must be an instance of Makeup class!")
    

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        self._date = date

    # TODO: calculate most popular makeup brand
    @classmethod
    def get_most_pop(cls):
        brand_frequencies = {}

        for purchase in cls.all:
            makeup = purchase.makeup_item
            brand = makeup.brand

            if brand in brand_frequencies:
                brand_frequencies[brand] += 1
            else: 
                brand_frequencies[brand] = 1

        # print(brand_frequencies)
        return max(brand_frequencies, key = brand_frequencies.get)

    def __repr__(self):
        return f"Purchaser: {self.person}\nMakeup Item: {self.makeup_item}\nDate: {self.date}"