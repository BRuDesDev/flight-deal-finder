import requests
from flight_data import FlightData

# Tequila Endpoint
TEQUILA_EP = "https://tequila-api.kiwi.com"
# Tequila API KEY
TEQUILA_API_KEY = "gLMpX7Fz0w-r9n-x2jQHv9-qGqg6h895"


class FlightSearch:
    """
    Class to handle all our interaction with Tequila API
    """
    def get_destination_code(self, city_name):
        """
        Get IATA code for the city and place it in Google Sheet

        :param city_name: name of city to get code
        :return: IATA code of city
        """
        location_endpoint = f"{TEQUILA_EP}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()['locations']
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, dest_city_code, from_time, to_time):
        """
        Check for flights within the time-frame, limited to cities in our sheet. Returns any flight data found.
        Will return "No flights found" if exception raised.
        """
        headers = {
            'apikey': TEQUILA_API_KEY
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": dest_city_code,
            "date_from": from_time.strftime('%d/%m/%Y'),
            "date_to": to_time.strftime('%d/%m/%Y'),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(
            url=f"{TEQUILA_EP}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {dest_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        # print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
