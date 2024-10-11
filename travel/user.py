class User:

    def __init__(self): #construct the object of the class
        self.name = None
        self.email = None
        self.type = 'guest'
        self.password_hash = None

     #  the set password method goes here
    def register(self, username,password,email):
        self.password=password
        self.username=username
        self.email=email

    def __repr__(self):
        s="Username: {}, Email: {}, Type: {}"
        s= s.format(self.username, self.email, self.type)
        return s


class FrequentTraveller(User):
    def __init__(self):
        self.type = 'Frequent Traveller'
        self.travellerID = None

    def register(self, username, password, email, travellerID):
        super().register(username, password, email)
        self.travellerID = travellerID

    def __repr__(self):
        s = super().__repr__()
        s = s + ", Traveller ID: {}".format(self.travellerID)
        return s


