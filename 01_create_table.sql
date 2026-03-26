-- create database hospital_project

-- drop table IF EXISTS hospital_data;

-- Create table hospital_data (
--     Name varchar(100) Default 'not Found',
--     Age int,
--     GENDER varchar(10),
--     "Blood Type" varchar(10),
--     "Medical Condition" varchar(255),
--     "Doctor" varchar (255),
--     Hospital VARCHAR(100),
--     "Insurance Provider" varchar(150),
--     "Billing Amount" decimal(15,2),
--     "Room Number" int,
--     "Admission Type" varchar(50),
--     "Medication" VARCHAR(150),
--     "Test Results" varchar(150),
--     "Date of Admission" TIMESTAMP NOT NULL,
--     "Discharge Date" TIMESTAMP UNIQUE,
-- )


-- Select * from information_schema.tables where table_name = 'main';

-- SELECT Count(*) from hospital_data;

-- drop table hospital_data;

-- CREATE INDEX idx_date_of_admission ON hospital_data ("Date of Admission");
-- CREATE INDEX idx_medical_condition ON hospital_data ("Medical Condition");


-- create table subset1k as select * from hospital_data limit 1000;
-- create table subset10k as select * from hospital_data limit 10000;

-- drop table subset1k;
-- drop table subset10k;

-- SELECT Count(*) from hospital_data;
-- SELECT Count(*) from subset1k;
-- SELECT Count(*) from subset10k;



-- select * from subset1k;
-- select * from subset10k;



-- select * from subset1k;

-- select * from subset1k where age < 50 
-- order by "Medical Condition";


-- create database backup_project;

-- create Role Andy with LOGIN PASSWORD 'andy@123';
-- create Role Ali with LOGIN PASSWORD 'ali@123';

-- GRANT CONNECT ON DATABASE hospital_project TO ali;
-- GRANT CONNECT ON DATABASE hospital_project TO andy;

-- GRANT USAGE ON SCHEMA public TO ali;

-- GRANT pg_read_all_data TO Andy;
-- GRANT pg_read_all_data TO Ali;
-- GRANT pg_write_all_data TO Ali;

-- REVOKE ALL ON DATABASE hospital_project FROM PUBLIC;
-- REVOKE CREATE ON SCHEMA public FROM PUBLIC;
-- SELECT current_user;

-- select count(*) from hospital_data;

-- TRUNCATE table hospital_data;

-- create table main as select * from hospital_data limit 0;

-- select * from main;

