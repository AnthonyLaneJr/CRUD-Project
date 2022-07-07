from flask import(
    Flask,
    request
)

from datetime import datetime
from app.database import user, reports



app = Flask(__name__)

VERSION = "1.0.0"


@app.get("/ping")
def ping():
    out = {
        "status":"ok",
        "message":"pong"
    }
    return out


@app.get("/version")
def get_version():
    out = {
        "status":"ok",
        "verison":VERSION,
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return out


@app.get("/users")
def get_all_users():
    user_list = user.scan()
    out = {
        "status":"ok",
        "users": user_list
    }
    return out


@app.get("/users/<int:pk>")
def get_user_by_id(pk):
    record = user.select_by_id(pk)
    out = {
        "status":"ok",
        "user":record
    }
    return out

@app.post("/users")
def create_user():
    user_data = request.json  # request context object
    user.insert(user_data)
    return "",204


@app.put("/users/<int:pk>")
def update_user(pk):
    user_data = request.json
    user.update(user_data, pk)
    return "",204


@app.delete("/users/<int:pk>")
def delete_user(pk):
    user.deactivate(pk)
    return "", 204

# ----- Vehicle Section -----    

@app.get("/reports/cars")
def users_and_vehicles():
    vehicle_report = reports.scan()
    out = {
        "status":"ok",
        "users": vehicle_report
    }
    return out

@app.get("/reports/cars/<int:pk>")
def get_vehicle_by_id(pk):
    record = reports.select_vehicle_by_id(pk)
    out = {
        "status":"ok",
        "Vehicle":record
    }
    return out

@app.post("/reports/cars")
def create_vehicle():
    vehicle_data = request.json  # request context object
    reports.insert_vehicle(vehicle_data)
    return "",204    

@app.put("/reports/cars/<int:pk>")
def update_reports(pk):
    reports_data = request.json
    reports.update(reports_data, pk)
    return "",204

@app.delete("/reports/cars/<int:pk>")
def delete_vehicle(pk):
    reports.deactivate_vehicle(pk)
    return "", 204