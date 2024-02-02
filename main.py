from sheets import Auth
from flight_search import FlightSearch
from notification_manager import NotificationManager

data = Auth()
search = FlightSearch()

search.codes()
search.search_flight_price()

manager = NotificationManager()

manager.send_data()
