

class FlightData:
    """
    A class to construct our data, to easily feed it to FlightSearch API.
    """
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        """
        Constructs all necessary attributes for our data, returns FlightData object.
        """
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

