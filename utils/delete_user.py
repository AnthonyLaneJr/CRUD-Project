import requests

URL = "http://127.0.0.1:5000/users/"

def delete_user(id):

    response = requests.delete(f"{URL}/{id}")
    if response.status.code == 204:
        print("User Successfully Deleted.")
    else:
        print("Error: User was not deleted.")

if __name__ == "__main__": #__main__ is the name of the terminal
    print("Delete USER")
    print("-" * 20)

    id = input("User id: ")

    delete_user(id)