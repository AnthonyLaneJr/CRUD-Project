from flask import g  # g stand for global -send and recieves data to different points within the applciation- while the application is running.
import sqlite3


DATABASE_URL = "user_crud.db"


def get_db():
    db = g.getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE_URL)
    return db