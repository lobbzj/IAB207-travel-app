import datetime

class Booking:

    def __init__(self, start_date, end_date, city, user):
        self.start_date = start_date
        self.end_date = end_date
        self.city = city
        self.user = user
        self.num_guests = 1
    
    def __repr__(self):
        return f'Start date:{self.start_date},\n End date:{self.end_date},\n Destination:{self.city},\n User:{self.user},\n Number of guests:{self.num_guests}'
    

