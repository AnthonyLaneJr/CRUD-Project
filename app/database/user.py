from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        user = {}
        user["id"] = result[0]
        user["first_name"] = result[1]
        user["last_name"] = result[2]
        user["hobbies"] = result[3]
        user["active"] = result[4]
        out.append(user)
    return out

def scan():
    cursor = get_db().execute(
        "SELECT * FROM user WHERE active=1", ())
    results = cursor.fetchall() #fetchall helps cursor select specific columsn and puts it in a list for python. like JSON for strings and data implementation
    cursor.close()
    return output_formatter(results)

def select_by_id(id):
    cursor = get_db().execute(
        "SELECT * FROM user WHERE id=? AND ACTIVE=1", (id, )
    )
    results = cursor.fetchall()
    cursor.close() #closes databse connection to let other users acces. 1024 is sqlite3 defaults amount of connection.
    return output_formatter(results) 

def insert(data):
    """ Create a new record in the user table """

    query = """INSERT INTO user (
        first_name, 
        last_name, 
        hobbies
        ) VALUES (?, ?, ?)
        """
    values = (
        data.get("first_name"),
        data.get("last_name"),
        data.get("hobbies")
    )
    cursor = get_db()
    cursor.execute(query, values)
    cursor.commit() #apply changes 
    cursor.close()


def deactivate(id):
    cursor = get_db()
    cursor.execute(
        "UPDATE user SET ACTIVE=0 WHERE id=?", (id, )
    )
    cursor.commit()
    cursor.close()
#sql:
#UPDATE USER SET ACTIVE=0 WHERE id=?