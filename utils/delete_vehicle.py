import requests

URL = "http://127.0.0.1:5000/reports/cars/"

def delete_vehicle(id):

    response = requests.delete(f"{URL}/{id}")
    if response.status.code == 204:
        print("Vehicle Successfully Deleted.")
    else:
        print("Error: Vehicle was not deleted.")

if __name__ == "__main__": #__main__ is the name of the terminal
    print("Delete Vehicle")
    print("-" * 20)

    id = input("Vehicle id: ")

    delete_vehicle(id)