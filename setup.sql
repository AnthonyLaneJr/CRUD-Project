

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

--- vehicles ---

CREATE TABLE vehicle_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(45)
);

CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    v_type VARCHAR(45) NOT NULL,
    license_plate VARCHAR(45) NOT NULL,
    color VARCHAR(45),
    brand VARCHAR(45) NOT NULL,
    model VARCHAR(45) NOT NULL,
    active BOOLEAN DEFAULT 1,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (v_type) REFERENCES vehicle_type(id)
);

INSERT INTO vehicle_type (description) VALUES("motorcycle");
INSERT INTO vehicle_type (description) VALUES("car");
INSERT INTO vehicle_type (description) VALUES("truck");
INSERT INTO vehicle_type (description) VALUES("suv");

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    user_id,
    brand,
    model
) VALUES (
    "red",
    "HELLO1",
    1,
    1,
    "honda",
    "something"
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    user_id,
    brand,
    model
) VALUES (
    "black",
    "HELLO1",
    4,
    1,
    "Ford",
    "Explorer"
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    user_id,
    brand,
    model
) VALUES (
    "gray",
    "HELLO1",
    2,
    2,
    "Kia",
    "Soul"
);

SELECT  user.last_name,
        user.first_name,
        user.hobbies,
        user.active,
        vehicle.license_plate,
        vehicle.color,
        vehicle_type.description,
        vehicle.brand,
        vehicle.model
FROM user
INNER JOIN vehicle ON user.id = vehicle.user_id
INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id;