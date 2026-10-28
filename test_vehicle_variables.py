
def test_vehicle_variables():

    # String
    vehicle_name = "Honda City"
    page_url = "https://supplier.uber.com/"
    page_text = "Vehicles (Beta)"

    # Integer
    vehicle_name_length = len(vehicle_name)

    # Boolean
    test_passed = True

    print("Vehicle Name:", vehicle_name)
    print("Vehicle Name Type:", type(vehicle_name))

    print("Vehicle Name Length:", vehicle_name_length)
    print("Length Type:", type(vehicle_name_length))

    print("Page URL:", page_url)
    print("Page Text:", page_text)

    print("Test Passed:", test_passed)
    print("Test Result Type:", type(test_passed))
