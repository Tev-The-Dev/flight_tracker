from amadeus import Client, Location, ResponseError
import os
from dotenv import load_dotenv
load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.id = os.getenv('AMADEUS_API_KEY')
        self.secret = os.getenv('AMADEUS_API_SECRET')
        #initialize the client
        self.client = Client(
            client_id = self.id,
            client_secret = self.secret
        )

    def search_flights(self):
        try:
            response = self.client.get(
                "/v2/shopping/flight-offers",
                originLocationCode="DFW",
                destinationLocationCode="NRT",
                departureDate="2025-05-21",
                adults=1,
                max=1,
            )
            print(response.result)  # Use result for parsed JSON response
        except ResponseError as error:
            print(f"Error Code: {error.code} - {error.description}")






    # base_url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
    # parameters = {
    #     "originLocationCode":"DFW",
    #     "destinationLocationCode":"NYC",
    #     "departureDate":"2025-05-20",
    #     "adults":1,
    # }
    # try:
    #     response = self.client.get(base_url, params=parameters)
    #     print(response.data)
    # except ResponseError as error:
    #     print(f"Error Code: {error}")









