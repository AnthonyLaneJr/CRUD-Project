from xml.dom.minidom import Document
from flask import (
    Flask,
    render_template,
    json,
)

import requests

BACKEND_URL = "http://127.0.0.1:5000"


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/about")
def about():
    out = {
        "up": False
    }
    ping_url = "%s/%s" % (BACKEND_URL, "ping")
    up = requests.get(ping_url)
    if up.status_code == 200:
        out["up"] = True
        version_url = "%s/%s" % (BACKEND_URL, "version")
        version_response = requests.get(version_url)
        version_json = version_response.json()
        out["version"] = version_json.get("version")
    return render_template("about.html", content=out)

@app.get("/users")
def users():
    user_url = "%s/%s" % (BACKEND_URL, "users")
    response = requests.get(user_url)
    if response.status_code == 200:
        response_json = response.json()
        user_list = response_json.get("users")
        return render_template("user_list.html", users=user_list)
    else:
        return render_template("error.html")

@app.get("/users/<int:pk>")
def delete_user(pk):
    delete_url = "%s/%s" % (BACKEND_URL, f"users/{pk}")
    response = requests.delete(delete_url)
    if response.status_code == 204:
        return render_template("delete.html", userID=pk)
    else:
        return render_template("error.html")

@app.get("/users/update")
def update_user():
    update_url = "%s/%s" % (BACKEND_URL, "users")
    # response = requests.put(update_url)
    return render_template("update.html")

@app.route("/users/create", methods=['GET','POST'])
def create_user():
    create_user_url = "%s/%s" % (BACKEND_URL, "users")
    response = requests.post(create_user_url)
    return render_template("create.html")




@app.route("/create/request", methods=['GET','POST'])
def send_user_create_request():
    send_user_create_request = "%s/%s" % (BACKEND_URL, "users")
    response = requests.post("http://127.0.0.1:5000/users")
    if response.status_code == 204:
        return render_template("create.html")
    
    


#request.form