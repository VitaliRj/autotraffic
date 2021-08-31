import requests
import pandas as pd

class Autobahn:
    """A API wrapper class for the Autobahn App API https://autobahn.api.bund.dev/.

    This class provides you with current administrative data in the form of
    construction site information, warnings, webcams, electric charging station, 
    resting areas and closures.

    To use:
    1.) Initialize the class, it can take a specific server/endpoint.
    CurrentlyThe default server is server="https://verkehr.autobahn.de/o/autobahn/".
    >>> api = autotraffic.Autobahn()
    2.) Get all highways in germany
    >>> highways = api.get_highways()
            roads
        0	A1
        1	A2
        2	A3
        3	A4
    3.) Get e.g. all webcams for a specific road.
    >>> webcams = api.get_webcams('A1')
    4.) Get details for a specidic webcam.
    >>> webcam_details = api.get_webcams_details(webcam_id)

    And so on...
    """
    def __init__(self, server="https://verkehr.autobahn.de/o/autobahn/"):
        self.server = server

    def get_highways(self):
        """ Returns a pandas.DataFrame with available highways in germany.
        Args:
            None
        Returns:
            [pandas.DataFrame] if request is successful, a pandas.DataFrame with available highways
            else the response.status_code.
        """
        response = requests.request("GET", self.server)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
            
        else:
            print(response.status_code)
            return response.status_code


    # ----------- Road Works ----------- #
    def get_roadworks(self, road_id: str):
        """ Returns a pandas.DataFrame of the current construction for a given highway.
        Args:
            [string] road_id: a string refering to a highway e.g. 'A1'
        Returns:
            [pandas.DataFrame] if request is successful, a pandas.DataFrame with roadworks,
            else the None.
        """
        url = f"https://verkehr.autobahn.de/o/autobahn/{road_id}/services/roadworks"

        response = requests.request("GET", url)

        if response.status_code == 200:
            return pd.DataFrame(response.json()['roadworks'])
        else:
            print(response.status_code)
            return response.status_code

    def get_roadwork_details(self, roadwork_id: str):
        """ Returns a details for a given roadwork identifier.
        Args:
            [string] roadwork_id: a string refering to a roadwork identifier
        Returns:
            [dict] if request is successful, a dict with details for a given roadwork_id,
            else the response.status_code.
        """
        url = f"https://verkehr.autobahn.de/o/autobahn/details/roadworks/{roadwork_id}"

        response = requests.request("GET", url)

        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            return response.status_code


    # ----------- Webcams ----------- #
    def get_webcams(self, road_id: str):
        """ Returns a pandas.DataFrame with available webcams for a given highway.
        Args:
            [string] road_id: a string refering to a highway e.g. 'A1'
        Returns:
            [pandas.DataFrame] if request is successful, a pandas.DataFrame with available webcams,
            else the response.status_code.
        """
        url = f"https://verkehr.autobahn.de/o/autobahn/{road_id}/services/webcam"

        response = requests.request("GET", url)

        if response.status_code == 200:
            return pd.DataFrame(response.json()['webcam'])
        else:
            print(response.status_code)
            return response.status_code

    def get_webcams_details(self, webcam_id: str):
        """ Returns a details for a given webcam identifier.
        Args:
            [string] webcam_id: a string refering to a webcam identifier
        Returns:
            [dict] if request is successful, a dict with details for a given webcam_id,
            else the response.status_code.
        """
        url = f"https://verkehr.autobahn.de/o/autobahn/details/webcam/{webcam_id}"

        response = requests.request("GET", url)

        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            return response.status_code


    # ----------- Resting Areas ----------- #
    def get_resting_areas(self, road_id: str):
        """ Returns a pandas.DataFrame of possible resting areas along a given highway.
        Args:
            [string] road_id: a string refering to a highway e.g. 'A1'
        Returns:
            [pandas.DataFrame] if request is successful, a pandas.DataFrame with resting areas
            along a given road_id, else the response.status_code.
        """
        url = f"https://verkehr.autobahn.de/o/autobahn/{road_id}/services/parking_lorry"

        response = requests.request("GET", url)

        if response.status_code == 200:
            return pd.DataFrame(response.json()['parking_lorry'])
        else:
            print(response.status_code)
            return response.status_code

    def get_resting_area_details(self, rest_id: str):
        """ Returns resting areas details for a given resting area identifier.
        Args:
            [string] road_id: a string refering to a highway e.g. 'A1'
        Returns:
            [dict] if request is successful, a dict with details for a given rest_id,
            else the response.status_code.
        """
        url = f"https://verkehr.autobahn.de/o/autobahn/details/parking_lorry/{rest_id}"

        response = requests.request("GET", url)

        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            return response.status_code


    # ----------- Warnings ----------- #
    def get_warnings(self, road_id: str):
        """ Returns a pandas.DataFrame of current warnings for a given highway.
        Args:
            [string] road_id: a string refering to a highway e.g. 'A1'
        Returns:
            [pandas.DataFrame] if request is successful, a pandas.DataFrame with resting areas
            along a given road_id, else the response.status_code.
        """
        url = f"https://verkehr.autobahn.de/o/autobahn/{road_id}/services/warning"

        response = requests.request("GET", url)

        if response.status_code == 200:
            return pd.DataFrame(response.json()['warning'])
        else:
            print(response.status_code)
            return response.status_code

    def get_warning_details(self, warning_id: str):
        """ Returns warning details for a given warning identifier.
        Args:
            [string] warning_id: a string refering to a highway e.g. 'A1'
        Returns:
            [dict] if request is successful, a dict with details for a given warning_id,
            else the response.status_code.
        """
        url = f"https://verkehr.autobahn.de/o/autobahn/details/warning/{warning_id}"

        response = requests.request("GET", url)

        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            return response.status_code


    # ----------- Closures ----------- #
    def get_closures(self, road_id):
        """ Returns a pandas.DataFrame of current closures for a given highway.
        Args:
            [string] road_id: a string refering to a highway e.g. 'A1'
        Returns:
            [pandas.DataFrame] if request is successful, a pandas.DataFrame with closures
            along a given road_id, else the response.status_code.
        """
        url = f"https://verkehr.autobahn.de/o/autobahn/{road_id}/services/closure"

        response = requests.request("GET", url)

        if response.status_code == 200:
            return pd.DataFrame(response.json()['closure'])
        else:
            print(response.status_code)
            return response.status_code

    def get_closure_details(self, closure_id: str):
        """ Returns closures details for a given closure identifier.
        Args:
            [string] closure_id: a string refering to a highway e.g. 'A1'
        Returns:
            [dict] if request is successful, a dict with details for a given closures,
            else the response.status_code.
        """
        url = f"https://verkehr.autobahn.de/o/autobahn/details/closure/{closure_id}"

        response = requests.request("GET", url)

        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            return response.status_code


    # ----------- Charging Stations----------- #
    def get_charging_stations(self, road_id: str):
        """ Returns a pandas.DataFrame of charging stations for a given highway.
        Args:
            [string] road_id: a string refering to a highway e.g. 'A1'
        Returns:
            [pandas.DataFrame] if request is successful, a pandas.DataFrame with charging stations
            along a given road_id, else the response.status_code.
        """
        url = f"https://verkehr.autobahn.de/o/autobahn/{road_id}/services/electric_charging_station"

        response = requests.request("GET", url)

        if response.status_code == 200:
            return pd.DataFrame(response.json()['electric_charging_station'])
        else:
            print(response.status_code)
            return response.status_code

    def get_charging_station_details(self, charging_station_id: str):
        """ Returns charging station details for a given closure identifier.
        Args:
            [string] closure_id: a string refering to a highway e.g. 'A1'
        Returns:
            [dict] if request is successful, a dict with details for a given charging station,
            else the response.status_code.
        """
        url = f"https://verkehr.autobahn.de/o/autobahn/details/electric_charging_station/{charging_station_id}"

        response = requests.request("GET", url)

        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            return response.status_code