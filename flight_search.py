import requests

TEQUILA_EP = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "gLMpX7Fz0w-r9n-x2jQHv9-qGqg6h895"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_EP}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()['locations']
        code = results[0]["code"]
        return code


