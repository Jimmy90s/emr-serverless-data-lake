-- create database
CREATE DATABASE IF NOT EXISTS crimes;

-- create table; 
CREATE EXTERNAL TABLE crimes.chicago_crimes
    (
	`ID` INT,
	`Case Number` STRING,
	`Date` DATE,
	`Block` STRING,
	`Primary Type` STRING,
	`Description` STRING,
	`Location Description` STRING,
	`Arrest` STRING,
	`Domestic` STRING,
	`Beat` INT,
	`District` INT,
	`Ward` INT,
	`Community Area` INT,
	`FBI Code`  STRING,
	`Latitude` FLOAT,
 	`Longitude` FLOAT
    )
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://james-laurie-emr/output/'
TBLPROPERTIES ('skip.header.line.count'='1')
;
