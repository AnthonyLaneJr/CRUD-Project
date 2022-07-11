from crypt import methods
from pickle import GET
from flask import(
    Flask,
    request,
)

from datetime import datetime
from app.database import user, reports



app = Flask(__name__)

VERSION = "1.0.0"


@app.route("/ping", methods=['GET'])
def ping():
    out = {
        "status":"ok",
        "message":"pong"
    }
    return out


@app.route("/version", methods=['GET'])
def get_version():
    out = {
        "status":"ok",
        "verison":VERSION,
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return out


@app.route("/users", methods=['GET'])
def get_all_users():
    user_list = user.scan()
    out = {
        "status":"ok",
        "users": user_list
    }
    return out


@app.route("/users/<int:pk>", methods=['GET'])
def get_user_by_id(pk):
    record = user.select_by_id(pk)
    out = {
        "status":"ok",
        "user":record
    }
    return out

@app.route("/users", methods=['POST'])
def create_user():
    user_data = request.json  # request context object
    user.insert(user_data)
    return "",204


@app.route("/users/<int:pk>", methods=['POST'])
def update_user(pk):
    user_data = request.json
    user.update(user_data, pk)
    return "",204


@app.route("/users/<int:pk>", methods=['DELETE'])
def delete_user(pk):
    user.deactivate(pk)
    return "", 204

# ----- Vehicle Section -----    

@app.route("/reports/cars", methods=['GET'])
def users_and_vehicles():
    vehicle_report = reports.scan()
    out = {
        "status":"ok",
        "users": vehicle_report
    }
    return out

@app.route("/reports/cars/<int:pk>", methods=['GET'])
def get_vehicle_by_id(pk):
    record = reports.select_vehicle_by_id(pk)
    out = {
        "status":"ok",
        "Vehicle":record
    }
    return out

@app.route("/reports/cars", methods=['POST'])
def create_vehicle():
    vehicle_data = request.json  # request context object
    reports.insert_vehicle(vehicle_data)
    return "",204    

@app.route("/reports/cars/<int:pk>", methods=['PUT'])
def update_reports(pk):
    reports_data = request.json
    reports.update(reports_data, pk)
    return "",204

@app.route("/reports/cars/<int:pk>", methods=['DELETE'])
def delete_vehicle(pk):
    reports.deactivate_vehicle(pk)
    return "", 204