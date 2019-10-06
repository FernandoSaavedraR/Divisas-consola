import uuid
class Exchange:
    def __init__(self,exchange,value,country,uid=None):
        self.exchange = exchange
        self.value = value
        self.country = country
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return ['exchange','value','country','uid']