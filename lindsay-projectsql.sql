#### Create Database
CREATE footbook;

######## Create Tables

#### Create Users Table
CREATE TABLE users(
	id INT PRIMARY KEY NOT NULL,
	username TEXT NOT NULL,
	email TEXT NOT NULL,
	fname TEXT NOT NULL,
	lname TEXT NOT NULL,
	dob TEXT,
	postcode TEXT NOT NULL,
	country_code TEXT NOT NULL,
	user_permissions INT,
	signup_timestamp TEXT NOT NULL,
	image BLOB
	); 

#### Create Activities Table	
CREATE TABLE activities(
	id INT PRIMARY KEY NOT NULL,
	title TEXT NOT NULL,
	description TEXT NOT NULL,
	icon BLOB
	);
	
#### Create Following Table
CREATE TABLE following(
	follower INT references users(id),
	followee INT references users(id),
	timestamp TEXT NOT NULL
	);

#### Create milestones Table
CREATE TABLE milestones(
	id INT PRIMARY KEY NOT NULL,
	user INT references users(id),
	weight REAL,
	max_heartrate REAL,
	resting_blood_pressure REAL,
	height REAL,
	timestamp REAL NOT NULL
	);	
	
#### Create table metric_types
CREATE TABLE metric_types(
	id INT PRIMARY KEY NOT NULL,
	title TEXT NOT NULL,
	unit TEXT NOT NULL,
	description TEXT NOT NULL,
	conversion_formula TEXT NOT NULL
	);
	
#### Create table metrics
CREATE TABLE metrics(
	id INT PRIMARY KEY NOT NULL,
	user INT references users(id),
	activity INT references activities(id),
	metric_type INT references metric_types(id),
	value REAL NOT NULL,
	timestamp NUMERIC NOT NULL,
	submit_timestamp NUMERIC NOT NULL
	);
	
#### Create table activities_metrics_types
CREATE TABLE activities_metrics_types(
	activity INT references users(id),
	metric_type TEXT references metric_types(id),
	activity_order INT
	); 
	

	
	