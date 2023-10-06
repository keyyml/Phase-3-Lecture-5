class Purchase():

    def __init__(self, person, makeup_item, date):
        self._person = person
        self._makeup_item = makeup_item
        self._date = date

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        self._date = date