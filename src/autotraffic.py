import requests
import pandas as pd

class Autobahn:
    """ A Autobahn GmbH API client that returns easy to use DataFrames with information about the german Autobahns.
    """
    def __init__(self, server="https://verkehr.autobahn.de/o/autobahn/"):
        self.server = server

    def get_highways(self):
        """ Returns a pandas.DataFrame with available highways in germany.
        Args:
            None
        Returns:
            [pandas.DataFrame] a pandas.DataFrame with available highways
            if request is successful, else the None.
        """
        response = requests.request("GET", self.server)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
            
        else:
            print(response.status_code)
            return None

    def get_webcams(self, road_id):
        """ Returns a pandas.DataFrame with available webcams for a given road_id
        Args:
            [string] road_id: a string refering to a highway e.g. 'A1'
        Returns:
            [pandas.DataFrame] a pandas.DataFrame with available webcams
            if request is successful, else the None.
        """
        url = f"https://verkehr.autobahn.de/o/autobahn/{road_id}/services/webcam"

        response = requests.request("GET", url)

        if response.status_code == 200:
            return pd.DataFrame(response.json()['webcam'])
        else:
            print(response.status_code)
            return None

    def get_roadworks(self,road_id):
        """ Returns a pandas.DataFrame of the current construction sites.
        Args:
            [string] road_id: a string refering to a highway e.g. 'A1'
        Returns:
            [pandas.DataFrame] a pandas.DataFrame with available webcams
            if request is successful, else the None.
        """
        url = f"https://verkehr.autobahn.de/o/autobahn/{road_id}/services/roadworks"

        response = requests.request("GET", url)

        if response.status_code == 200:
            return pd.DataFrame(response.json()['roadworks'])
        else:
            print(response.status_code)
            return None