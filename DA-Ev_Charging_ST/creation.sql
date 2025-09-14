create database Ev_charging;
use Ev_charging

CREATE TABLE stations (
    Station_ID INT PRIMARY KEY,
    Location VARCHAR(100),
    Capacity_kW INT,
    Installation_Date DATE,
    Power_Level VARCHAR(20)
);

CREATE TABLE vehicles (
    Vehicle_ID INT PRIMARY KEY,
    Station_ID INT,
    Vehicle_Type VARCHAR(50),
    Battery_Capacity_kWh FLOAT,
    Manufacturer VARCHAR(50),
    Model_Name VARCHAR(100),
    Registration_Year INT,
    Owner_Type VARCHAR(50),
    FOREIGN KEY (Station_ID) REFERENCES stations(Station_ID)
);
CREATE TABLE charging_sessions (
    Session_ID INT PRIMARY KEY,
    Station_ID INT,
    Vehicle_ID INT,
    Start_Time DATETIME,
    End_Time DATETIME,
    Energy_Consumed_kWh FLOAT,
    Payment_Amount FLOAT,
    Charging_Mode VARCHAR(20),
    Session_Status VARCHAR(20),
    FOREIGN KEY (Station_ID) REFERENCES stations(Station_ID),
    FOREIGN KEY (Vehicle_ID) REFERENCES vehicles(Vehicle_ID)
);
CREATE TABLE weather (
    Weather_ID INT PRIMARY KEY,
    Timestamp DATETIME,
    Location VARCHAR(100),
    Temperature_C FLOAT,
    Rainfall_mm FLOAT,
    Wind_Speed_kph FLOAT,
    Humidity_pct FLOAT,
    Weather_Condition VARCHAR(20)
);
select count(*) as total_s from stations;
select count(*) as vehi_c from vehicles;
select count(*) as charging_t from charging_sessions;
select count(*) as we_t from weather;

-- Peak Usage hours:
SELECT HOUR(start_time) AS hour, COUNT(*) AS sessions_count
FROM charging_sessions
GROUP BY HOUR(start_time)
ORDER BY sessions_count DESC;

-- Most Active Vehicles

SELECT Vehicle_ID, COUNT(*) AS Sessions
FROM charging_sessions
GROUP BY Vehicle_ID
ORDER BY Sessions DESC
LIMIT 10;

-- Charging Sessions During Rain

SELECT COUNT(*) AS Rainy_Sessions
FROM charging_sessions cs
JOIN stations s ON cs.Station_ID = s.Station_ID
JOIN weather w ON s.Location = w.Location AND DATE(cs.Start_Time) = DATE(w.Timestamp)
WHERE w.Weather_Condition IN ('Rainy', 'Stormy');

-- Revenue per Station

SELECT Station_ID, SUM(Payment_Amount) AS Total_Revenue
FROM charging_sessions
GROUP BY Station_ID
ORDER BY Total_Revenue DESC;

-- Station Utilization by Location

SELECT s.Location, COUNT(cs.Session_ID) AS Sessions
FROM charging_sessions cs
JOIN stations s ON cs.Station_ID = s.Station_ID
GROUP BY s.Location
ORDER BY Sessions DESC;

-- Top Manufacturers by Energy Consumption

SELECT v.Manufacturer, SUM(cs.Energy_Consumed_kWh) AS Total_Energy
FROM charging_sessions cs
JOIN vehicles v ON cs.Vehicle_ID = v.Vehicle_ID
GROUP BY v.Manufacturer
ORDER BY Total_Energy DESC;

-- Sessions per Station
SELECT Station_ID, COUNT(*) AS Total_Sessions
FROM charging_sessions
GROUP BY Station_ID
ORDER BY Total_Sessions DESC;