import requests

# Sheety API
SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/663efd931701f70a32b6be03e30990ed/flightDeals/prices'


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and return it
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        # make a PUT request and update the Google Sheet with the IATA codes
        for city in self.destination_data:
            # Data to add to each row
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)




