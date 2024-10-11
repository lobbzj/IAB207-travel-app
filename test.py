from travel.user import User, FrequentTraveller
from travel.booking import Booking
from datetime import datetime
from travel.city import City

# Create a user
user = FrequentTraveller()
user.register('John Doe', ' qwerty', '123@qq.com', '123456')
print(user)
# Create a city
city = City('Nairobi', 'the city in the sun')
print(city)
# Create a booking
booking = Booking(datetime(2020, 1, 1), datetime(2020, 1, 3), city, user)
print(booking)