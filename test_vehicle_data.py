
from utilities.json_reader import JsonReader


def test_read_vehicle_data():
    vehicle_data = JsonReader.get_data(
        "vehicle_data.json",
        "invalid_vehicle"
    )

    vehicle_name = vehicle_data["name"]

    print(vehicle_name)
