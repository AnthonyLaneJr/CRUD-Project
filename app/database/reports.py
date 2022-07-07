from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        user = {}
        user["last_name"] = result[0]
        user["first_name"] = result[1]
        user["hobbies"] = result[2]
        user["active"] = result[3]
        user["license_plate"] = result[4]
        user["color"] = result[5]
        user["description"] = result[6]
        user["brand"] = result[7]
        user["model"] = result[8]
        out.append(user)
    return out

def scan():
    cursor = get_db().execute(
        """SELECT  user.last_name,
        user.first_name,
        user.hobbies,
        vehicle.active,
        vehicle.license_plate,
        vehicle.color,
        vehicle_type.description,
        vehicle.brand,
        vehicle.model
        FROM user
        INNER JOIN vehicle ON user.id = vehicle.user_id
        INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id
        WHERE vehicle.active=1;""", ())
    results = cursor.fetchall() #fetchall helps cursor select specific columsn and puts it in a list for python. like JSON for strings and data implementation
    cursor.close()
    return output_formatter(results)

def select_vehicle_by_id(id):
    cursor = get_db().execute(
        """SELECT  user.last_name,
        user.first_name,
        user.hobbies,
        vehicle.active,
        vehicle.license_plate,
        vehicle.color,
        vehicle_type.description,
        vehicle.brand,
        vehicle.model
        FROM user
        INNER JOIN vehicle ON user.id = vehicle.user_id
        INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id
        WHERE vehicle.id=?
        ;""", (id, ))
    results = cursor.fetchall()
    cursor.close() #closes databse connection to let other users acces. 1024 is sqlite3 defaults amount of connection.
    return output_formatter(results) 

def insert_vehicle(data):
    """ Create a new record in the user table """

    query = """INSERT INTO vehicle (
        color,
        v_type,
        license_plate,
        user_id,
        brand,
        model
        ) VALUES (?, ?, ?, ?, ?, ?)
        """
    values = (
        data.get("color"),
        data.get("v_type"),
        data.get("license_plate"),
        data.get("user_id"),
        data.get("brand"),
        data.get("model")
    )
    cursor = get_db()
    cursor.execute(query, values)
    cursor.commit() #apply changes 
    cursor.close()


def deactivate_vehicle(id):
    cursor = get_db()
    cursor.execute(
        "UPDATE vehicle SET ACTIVE=0 WHERE id=?", (id, )
    )
    cursor.commit()
    cursor.close()
#sql:
#UPDATE USER SET ACTIVE=0 WHERE id=?