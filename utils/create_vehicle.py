import requests

URL = "http://127.0.0.1:5000/reports/cars"


def create_vehicle(color, vicType, licensePlate, userId, brand, model):
    user_data = {
        "color" : color,
        "v_type" : vicType,
        "license_plate" : licensePlate,
        "user_id" : userId,
        "brand" : brand,
        "model" : model
    }

    response = requests.post(URL, json=user_data)
    if response.status.code == 204:
        print("Vehicle Successfully created.")
    else:
        print("Error: Vehicle was not created.")


#if the script is dirrectly executed form the termianl
if __name__ == "__main__": #__main__ is the name of the terminal
    print("CREATE Vehicle")
    print("-" * 20)

    color = input("Color: ")
    vicType = input("Vehicle Type: ")
    licensePlate = input("License Plate: ")
    userId = input("User ID: ")
    brand = input("Brand: ")
    model = input("Model: ")

    create_user(color, vicType, licensePlate, userId, brand, model)