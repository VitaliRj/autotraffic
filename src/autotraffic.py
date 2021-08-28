import requests
import pandas as pd

class Autobahn:
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
    def get_roadworks(self, road_id):
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

    def get_roadwork_details(self, roadwork_id):
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
    def get_webcams(self, road_id):
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

    def get_webcams_details(self, webcam_id):
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


    # ----------- Resting Areas -----------
    def get_resting_areas(self, road_id):
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

    def get_resting_area_details(self, rest_id):
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


    # ----------- Resting Areas ----------- #
    def get_warnings(self, road_id):
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

    def get_warning_details(self, warning_id):
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
    #Todo
    # ----------- Charging Stations----------- #
    #Todo