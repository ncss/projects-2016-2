---- Create Database
--CREATE footbook;

-------- Create Tables

---- Create Users Table
CREATE TABLE users(
	id INTEGER PRIMARY KEY,
	username TEXT NOT NULL,
	email TEXT NOT NULL,
	fname TEXT NOT NULL,
	lname TEXT NOT NULL,
	dob TEXT,
	postcode TEXT NOT NULL,
	country_code TEXT NOT NULL,
	signup_timestamp INTEGER NOT NULL,
	image BLOB
	); 

---- Create Following Table
CREATE TABLE following(
	follower INTEGER references users(id),
	followee INTEGER references users(id),
	timestamp INTEGER NOT NULL
	);

---- Create table metrics
CREATE TABLE metrics(
	id INTEGER PRIMARY KEY,
	user INTEGER references users(id),
	activity INTEGER references activities(id),
	metric_type INTEGER references metric_types(id),
	value REAL NOT NULL,
	timestamp INTEGER NOT NULL,
	submit_timestamp INTEGER NOT NULL
	);

	/*

---- Create Activities Table	
CREATE TABLE activities(
	id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	description TEXT NOT NULL,
	icon BLOB
	);
---- Create milestones Table
CREATE TABLE milestones(
	id INTEGER PRIMARY KEY,
	user INTEGER references users(id),
	weight REAL,
	max_heartrate REAL,
	resting_blood_pressure REAL,
	height REAL,
	timestamp REAL NOT NULL
	);	
	
---- Create table metric_types
CREATE TABLE metric_types(
	id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	unit TEXT NOT NULL,
	description TEXT NOT NULL,
	conversion_formula TEXT NOT NULL
	);
	
	
---- Create table activities_metrics_types
--CREATE TABLE activities_metrics_types(
	activity INTEGER references users(id),
	metric_type TEXT references metric_types(id),
	activity_order INTEGER
	); 
	
	*/
	
	
