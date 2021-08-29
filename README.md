# Autotraffic
A Python package that provides you with up-to-date information about all German highways (Autobahn). The package provides traffic, electric charging stations, webcams, road works and closeures and more. It uses the API of Autobahn GmbH (https://autobahn.api.bund.dev/) and delivers the results in easy to use DataFrames.

## Installation

```python
pip install autotraffic
```

## Usage
```python
import autotraffic

# Initialize
api = autotraffic.Autobahn()
```

```python
# Get all highways (road_ids)
highways = api.get_highways()
highways

|     | roads   |
|----:|:--------|
|   0 | A1      |
|   1 | A2      |
|   2 | A3      |
```

Now you can request more information such as road works, webcams, warnings, resting/parking areas, closures and electric charging stations by using the road_id from the roads column of highways.

In addition, you can also retrieve specific details by using the identifier column values and get_..._details(identifier), as shown below.

### Road Works
```python
# ----------- Road Works ----------- #
road_id = 'A1'
roadworks = api.get_roadworks(road_id)

# Choose a specific roadwork (if not empty).
roadwork_id = roadworks['identifier'][0]
# Get some details
roadwork_details = api.get_roadwork_details(roadwork_id)
roadwork_details
```
```json
{
    "extent": "10.728384054665147,54.00605746113356,10.775848767524598,54.09436740278899",
    "identifier": "Uk9BRFdPUktTX19tZG0uc2hfXzYzMTU=",
    "routeRecommendation": [],
    "coordinate": {
        "lat": "54.006057",
        "long": "10.729057"
    },
    "footer": [],
    "icon": "123",
    "isBlocked": "false",
    "description": [
        "Beginn: 29.06.2021 09:00",
        "Ende: 28.11.2021 17:00",
        "",
        "Art der Ma\u00dfnahme:Asphaltdeckenerneuerung",
        "Einschr\u00e4nkungen:Es steht nur 1 Fahrstreifen zur Verf\u00fcgung.\n\nVollsperrung der AS Eutin Ostseite vom 17.07.2021 - 15.09.2021.\n\nVollsperrung der AS Scharbeutz Ostseite vom 16.09.2021 - 17.11.2021.",
        "Maximale Durchfahrsbreite: 3.25\n"
    ],
    "title": "A1 | AS Pansdorf (17) - AS Neustadt-Mitte (14)",
    "point": "10.729057,54.006057",
    "display_type": "ROADWORKS",
    "lorryParkingFeatureIcons": [],
    "future": false,
    "subtitle": "L\u00fcbeck Richtung Fehmarn",
    "startTimestamp": "2021-06-29T09:00:00.000+0200"
}
```

### Webcams
```python
# ----------- Webcams ----------- #
webcams = api.get_webcams(road_id)

# Choose a specific webcam (if not empty).
webcam_id = webcams['identifier'][0]

# Get some details
webcam_details = api.get_webcams_details(webcam_id)
webcam_details
```
```json
{
    "extent": "6.861151,50.987423,6.861151,50.987423",
    "identifier": "V0VCQ0FNX19OUldfU2lsYS1TaWduYWxiYXVfMTAxMDgxMDk4ODE2NDgyOTQ4NTQ=",
    "routeRecommendation": [],
    "coordinate": {
        "lat": "50.987423",
        "long": "6.861151"
    },
    "footer": [
        "ID: WEBCAM__NRW_Sila-Signalbau_10108109881648294854"
    ],
    "icon": "webcam",
    "isBlocked": "false",
    "description": [],
    "title": "A1 | ID005 AK K\u00f6ln-Nord",
    "operator": "NRW",
    "point": "6.861151,50.987423",
    "display_type": "WEBCAM",
    "lorryParkingFeatureIcons": [],
    "future": false,
    "imageurl": "https://www.verkehr.nrw/webcams/10108109881648294854.jpg",
    "subtitle": "Blickrichtung Dortmund",
    "linkurl": "https://www.blitzvideoserver.de/player_strassennrw.html?serverip=62.113.210.7&serverapp=strassennrw-rtplive&streamname=10108109881648294854"
}
```

### Warnings
```python
# ----------- Warnings ----------- #
road_id = 'A1'
warnings = api.get_warnings(road_id)

# Choose a specific warning (if not empty).
warning_id = warnings['identifier'][0]

# Get some details
warning_details = api.get_warning_details(warning_id)
warning_details
```
```json
{
    "extent": "9.80449,53.36979,9.86097,53.37301",
    "identifier": "V0FSTklOR19fbWRtLnZpel9fTE1TLU5JL3JfTE1TLU5JLzIyNjU5Ml9EICBOSSBMTVMtTkkgIC4w",
    "routeRecommendation": [],
    "coordinate": {
        "lat": "53.373010",
        "long": "9.860970"
    },
    "footer": [],
    "icon": "101",
    "isBlocked": "false",
    "description": [
        "Beginn: 29.08.2021 11:46",
        "",
        "A1, A261 Hamburg Richtung Hamburg-S\u00fcdwest",
        "in H\u00f6he Buchholzer Dreieck",
        "Unfall"
    ],
    "title": "A1 | AD Buchholzer Dreieck (43) - AS Rade (44)",
    "point": "9.860970,53.373010",
    "display_type": "WARNING",
    "lorryParkingFeatureIcons": [],
    "future": false,
    "subtitle": "Hamburg Richtung Bremen",
    "startTimestamp": "2021-08-29T11:46:38.000+0200"
}
```

### Resting Areas
```python
# ----------- Resting Areas ----------- #
road_id = 'A1'
resting_areas = api.get_resting_areas(road_id)

# Choose a specific resting area (if not empty).
resting_area_id = resting_areas['identifier'][0]

# Get some details
resting_area_details = api.get_resting_area_details(resting_area_id)
resting_area_details
```
```json
{
    "extent": "10.979849815368652,54.362571716308594,10.979849815368652,54.362571716308594",
    "identifier": "UEFSS0lOR19fbWRtLmxvcnJ5LnBhcmtpbmdfX0RFLVNILTAwMTEwOA==",
    "routeRecommendation": [],
    "coordinate": {
        "lat": "54.362572",
        "long": "10.979850"
    },
    "footer": [],
    "icon": "314-50",
    "isBlocked": "false",
    "description": [
        "PKW Stellpl\u00e4tze: 21 ",
        "LKW Stellpl\u00e4tze: 20 "
    ],
    "title": "A 1 | Richtung Puttgarden",
    "point": "10.979850,54.362572",
    "display_type": "PARKING",
    "lorryParkingFeatureIcons": [
        {
            "icon": "almofont almo-picnic_facility",
            "description": "Picknickm\u00f6glichkeiten",
            "style": ""
        },
        {
            "icon": "almofont almo-restroom",
            "description": "Toilette vorhanden",
            "style": ""
        }
    ],
    "future": false,
    "subtitle": "(Ostseeblick S)"
}
```
### Closures
```python
# ----------- Closures ----------- #
road_id = 'A1'
closures = api.get_closures(road_id)

# Choose a specific closure (if not empty).
closure_id = closures['identifier'][0]

# Get some details
closure_details = api.get_closure_details(closure_id)
closure_details
```
```json
{
    "extent": "8.020042501838338,52.3416333067941,8.043980021997255,52.394651600625224",
    "identifier": "Q0xPU1VSRV9fbWRtLm5pX18xNjY1MQ==",
    "routeRecommendation": [],
    "coordinate": {
        "lat": "52.341633",
        "long": "8.020043"
    },
    "footer": [],
    "icon": "250",
    "isBlocked": "false",
    "description": [
        "Beginn: 30.08.2021 19:00",
        "Ende: 03.09.2021 06:00",
        "(Ende der Gesamtma\u00dfnahme: 03.09.2021)",
        "",
        "L\u00e4nge: 6.38 km"
    ],
    "title": "A1 | AS Osnabr\u00fcck-Nord (70) - AS Bramsche (68)",
    "point": "8.020043,52.341633",
    "display_type": "CLOSURE",
    "lorryParkingFeatureIcons": [],
    "future": true,
    "subtitle": "Osnabr\u00fcck Richtung Bremen",
    "startTimestamp": "2021-08-30T19:00:00.000+0200"
}
```
### Charging Stations
```python
# ----------- Charging Stations ----------- #
road_id = 'A1'
charging_stations = api.get_charging_stations(road_id)

# Choose a specific charging station (if not empty).
charging_station_id = charging_stations['identifier'][0]

# Get some details
charging_station_details = api.get_charging_station_details(charging_station_id)
charging_station_details
```
```json
{
    "extent": "9.176298,53.090847,9.176298,53.090847",
    "identifier": "RUxFQ1RSSUNfQ0hBUkdJTkdfU1RBVElPTl9fMTI2OTk=",
    "routeRecommendation": [],
    "coordinate": {
        "lat": "53.090847",
        "long": "9.176298"
    },
    "footer": [],
    "icon": "charging_plug_strong",
    "isBlocked": "false",
    "description": [
        "A1 | Bremen | Rastst\u00e4tte Grundbergsee Nord",
        "27376 Sottrum",
        "",
        "Ladepunkt 1:",
        "AC Kupplung Typ 2",
        "43 kW",
        "",
        "Ladepunkt 2:",
        "DC Kupplung Combo, DC CHAdeMO",
        "50 kW"
    ],
    "title": "A1 | Bremen | Rastst\u00e4tte Grundbergsee Nord",
    "point": "9.176298,53.090847",
    "display_type": "STRONG_ELECTRIC_CHARGING_STATION",
    "lorryParkingFeatureIcons": [],
    "future": false,
    "subtitle": "Schnellladeeinrichtung"
}

```

##
