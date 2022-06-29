

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
)


--- insert data ----


INSERT INTO user (
    first_name,
    last_name,
    hobbies
    ) VALUES (
    "Anthony",
    "Lane",
    "Spartan Racing"
)

--- to read -----
SELECT * FROM seed

--- another insert ----
INSERT INTO user (
    first_name,
    last_name,
    hobbies
    ) VALUES (
    "Ricky",
    "Bobby",
    "Racing"
)