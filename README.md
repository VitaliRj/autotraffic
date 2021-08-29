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
```

```python
# ----------- Road Works ----------- #
road_id = 'A1'
roadworks = api.get_roadworks(road_id)

# Choose a specific roadwork (if not empty).
roadwork_id = roadworks['identifier'][0]
# Get some details
roadwork_details = api.get_roadwork_details(roadwork_id)
```

```python
# ----------- Webcams ----------- #
webcams = api.get_webcams(road_id)

# Choose a specific webcam (if not empty).
webcam_id = webcams['identifier'][0]

# Get some details
webcam_details = api.get_webcams_details(webcam_id)
```

```python
# ----------- Warnings ----------- #
road_id = 'A1'
warnings = api.get_warnings(road_id)

# Choose a specific warning (if not empty).
warning_id = warnings['identifier'][0]

# Get some details
warning_details = api.get_warning_details(warning_id)
```

```python
# ----------- Resting Areas ----------- #
road_id = 'A1'
resting_areas = api.get_resting_areas(road_id)

# Choose a specific resting area (if not empty).
resting_area_id = resting_areas['identifier'][0]

# Get some details
resting_area_details = api.get_resting_area_details(resting_area_id)
```

```python
# ----------- Closures ----------- #
road_id = 'A1'
closures = api.get_closures(road_id)

# Choose a specific closure (if not empty).
closure_id = closures['identifier'][0]

# Get some details
closure_details = api.get_closure_details(closure_id)
```

```python
# ----------- Charging Stations----------- #
road_id = 'A1'
charging_stations = api.get_charging_stations(road_id)

# Choose a specific charging station (if not empty).
charging_station_id = charging_stations['identifier'][0]

# Get some details
charging_station_details = api.get_charging_station_details(charging_station_id)
```

##

```python

```