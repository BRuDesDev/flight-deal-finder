"""
Program Requirements:

    2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities
    in the Google Sheet.

    3.If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number
    with the Twilio API.

    4.The SMS should include the departure airport IATA code, destination airport IATA code, departure city,
    destination city, flight price and flight dates. e.g.
"""

from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
print(sheet_data)