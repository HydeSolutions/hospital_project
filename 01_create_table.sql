-- create database hospital_project

-- drop table IF EXISTS hospital_data;

-- Create table hospital_data (
--     Name varchar(100),
--     Age int,
--     PRIMARY KEY ("Date of Admission"),
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
--     "Date of Admission" TIMESTAMP,
--     "Discharge Date" TIMESTAMP

-- )


-- Select * from information_schema.tables;

-- SELECT * from hospital_data



-- CREATE INDEX idx_date_of_admission ON hospital_data ("Date of Admission");
-- CREATE INDEX idx_medical_condition ON hospital_data ("Medical Condition");


-- create table subset1k as select * from hospital_data
-- create table subset10k as select * from hospital_data

-- drop table subset1k;
-- drop table subset10k;



-- select * from subset1k;
-- select * from subset10k;
