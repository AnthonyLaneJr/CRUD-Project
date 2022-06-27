from app.databse import get_db


def output_formatter(results):
    out = []
    for result in results:
        user = {}
        out["id"] = result[0]
        out["first_name"] = result[1]
        out["last_name"] = result[2]
        out["hobbies"] = result[3]
        out["active"] = result[4]
        out.append(user)
    return output_formatter

def scan():
    cursor = get_db().execute(
        "SELECT * FROM user WHERE active=1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)