CREATE TABLE inbox_status (
	temperature FLOAT,
	humidity INTEGER,
	date DATETIME
);

CREATE TABLE fan_status (
    id INT PRIMARY KEY,
    status BOOLEAN
);

CREATE TABLE thresholds (
    temperature FLOAT,
    humidity INTEGER
);