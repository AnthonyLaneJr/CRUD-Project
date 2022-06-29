import requests

URL = "http://127.0.0.1:5000/users"


def create_user(first, last, hobbies):
    user_data = {
        "first_name" : first,
        "last_name" : last,
        "hobbies" : hobbies
    }

    response = requests.post(URL, json=user_data)
    if response.status.code == 204:
        print("User Successfully created.")
    else:
        print("Error: User was not created.")


#if the script is dirrectly executed form the termianl
if __name__ == "__main__": #__main__ is the name of the terminal
    print("CREATE USER")
    print("-" * 20)

    first = input("First name: ")
    last = input("Last name: ")
    hobbies = input("Hobbies: ")

    create_user(first, last, hobbies)