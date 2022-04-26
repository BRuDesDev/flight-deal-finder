"""
Program Requirements:
    1. Create Google sheet, with list of cities and lowest price
    2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities
    in the Google Sheet.
    3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number
    with the Twilio API.
    4.The SMS should include the departure airport IATA code, destination airport IATA code, departure city,
    destination city, flight price and flight dates. e.g.
"""

from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = 'ORD'

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    # print(f"sheet_data:\n {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"⚠️Low price alert: ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} "
                    f"to {flight.destination_city}-{flight.destination_airport}, "
                    f"from {flight.out_date} to {flight.return_date}."
        )
