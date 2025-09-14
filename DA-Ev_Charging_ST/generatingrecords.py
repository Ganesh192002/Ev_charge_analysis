"""
import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration
num_rows = 20000
start_id = 10001
locations = [
    'Delhi', 'Mumbai', 'Bengaluru', 'Hyderabad', 'Chennai', 'Kolkata', 'Pune', 'Ahmedabad', 'Jaipur', 'Lucknow',
    'Coimbatore', 'Nagpur', 'Bhopal', 'Visakhapatnam', 'Surat', 'Thane', 'Patna', 'Vadodara', 'Ghaziabad', 'Ludhiana',
    'Agra', 'Nashik', 'Faridabad', 'Meerut', 'Rajkot', 'Kalyan', 'Vasai', 'Varanasi', 'Srinagar', 'Aurangabad',
    'Dhanbad', 'Amritsar', 'Navi Mumbai', 'Allahabad', 'Ranchi', 'Howrah', 'Jabalpur', 'Gwalior', 'Vijayawada',
    'Jodhpur', 'Madurai', 'Raipur', 'Kota', 'Guwahati', 'Chandigarh', 'Solapur', 'Hubli', 'Mysuru', 'Tiruchirappalli',
    'Bareilly', 'Moradabad', 'Noida', 'Tirunelveli', 'Kollam', 'Thrissur', 'Nellore', 'Belgaum', 'Guntur', 'Warangal',
    'Salem', 'Ujjain', 'Bokaro', 'Jamshedpur', 'Dehradun', 'Ajmer', 'Jhansi', 'Kakinada', 'Panipat', 'Bathinda',
    'Shimla', 'Bilaspur', 'Rewa', 'Satna', 'Silchar', 'Siliguri', 'Aligarh', 'Rohtak', 'Hisar', 'Ambala', 'Kurukshetra',
    'Hosur', 'Pimpri-Chinchwad', 'Tirupati', 'Anantapur', 'Karimnagar', 'Nanded', 'Bhagalpur', 'Muzaffarpur',
    'Saharanpur', 'Gaya', 'Darbhanga', 'Berhampur', 'Rourkela', 'Cuttack', 'Balasore', 'Durgapur', 'Asansol',
    'Imphal', 'Aizawl', 'Gangtok', 'Shillong', 'Kohima', 'Itanagar', 'Panaji', 'Gandhinagar', 'Naya Raipur',
    'Amaravati', 'Dharwad', 'Karnal', 'Porbandar', 'Tuticorin', 'Vizhinjam', 'Mangalore', 'Kochi', 'Paradip',
    # ... (add more to reach 300)
]
capacities = [3.3, 7.2, 11, 22, 30, 43, 50, 60, 75, 90, 100, 120, 150, 180, 200, 250, 300]

def generate_station_data(n):
    data = []
    for i in range(n):
        station_id = start_id + i
        location = random.choice(locations)
        capacity = random.choice(capacities)
        install_date = datetime.strptime('2019-01-01', '%Y-%m-%d') + timedelta(days=random.randint(0, 2100))
        if capacity <= 22:
            power_level = 'Level 1'
        elif capacity <= 100:
            power_level = 'Level 2'
        else:
            power_level = 'DC Fast'
        data.append({
            'Station_ID': station_id,
            'Location': location,
            'Capacity_kW': capacity,
            'Installation_Date': install_date.strftime('%Y-%m-%d'),
            'Power_Level': power_level
        })
    return pd.DataFrame(data)

# Generate and save
df_stations = generate_station_data(num_rows)
df_stations.to_excel('EV_Stations_20000.xlsx', index=False)
print("✅ EV Stations dataset saved as 'EV_Stations_20000.xlsx'")

import pandas as pd
import random

# Configuration
num_rows = 20000
start_vehicle_id = 50001
station_id_range = (10001, 30000)

# Expanded vehicle types
vehicle_types = [
    'Sedan', 'SUV', 'Hatchback', 'Truck', 'Van', 'Coupe', 'Convertible', 'Crossover',
    'Minivan', 'Pickup', 'Luxury Sedan', 'Compact SUV', 'Electric Scooter', 'Electric Bike', 'Three-Wheeler'
]

# Expanded owner types
owner_types = [
    'Individual', 'Fleet', 'Government', 'Corporate', 'Rental Agency', 'Ride-Sharing Partner',
    'Delivery Service', 'Taxi Operator', 'Municipal Utility', 'Educational Institution'
]

# Expanded manufacturers and models
manufacturers_models = {
    'Tata': ['Nexon EV', 'Tigor EV', 'Punch EV'],
    'Mahindra': ['eVerito', 'XUV400', 'BE.05'],
    'Hyundai': ['Kona Electric', 'Ioniq 5'],
    'MG': ['ZS EV', 'Comet EV'],
    'Tesla': ['Model 3', 'Model Y', 'Model S'],
    'BYD': ['Atto 3', 'e6', 'Seal'],
    'Kia': ['EV6', 'Soul EV'],
    'Mercedes-Benz': ['EQB', 'EQS', 'EQE'],
    'BMW': ['iX', 'i4', 'i7'],
    'Audi': ['e-tron', 'Q8 e-tron', 'Q4 e-tron'],
    'Volkswagen': ['ID.4', 'ID.3'],
    'Volvo': ['XC40 Recharge', 'C40 Recharge'],
    'Renault': ['ZOE', 'K-ZE'],
    'Nissan': ['Leaf', 'Ariya'],
    'Honda': ['e', 'Prologue'],
    'Ford': ['Mustang Mach-E', 'F-150 Lightning'],
    'Maruti Suzuki': ['eVX', 'Futuro-e'],
    'Citroën': ['ë-C3'],
    'Skoda': ['Enyaq iV'],
    'Jeep': ['Avenger EV']
}

# Generate synthetic vehicle data
def generate_vehicle_data(n):
    data = []
    for i in range(n):
        vehicle_id = start_vehicle_id + i
        station_id = random.randint(*station_id_range)
        vehicle_type = random.choice(vehicle_types)
        owner_type = random.choice(owner_types)
        manufacturer = random.choice(list(manufacturers_models.keys()))
        model_name = random.choice(manufacturers_models[manufacturer])
        battery_capacity = round(random.uniform(30, 100), 1)
        registration_year = random.randint(2018, 2025)

        data.append({
            'Vehicle_ID': vehicle_id,
            'Station_ID': station_id,
            'Vehicle_Type': vehicle_type,
            'Battery_Capacity_kWh': battery_capacity,
            'Manufacturer': manufacturer,
            'Model_Name': model_name,
            'Registration_Year': registration_year,
            'Owner_Type': owner_type
        })
    return pd.DataFrame(data)

# Generate and save to Excel
df_vehicles = generate_vehicle_data(num_rows)
df_vehicles.to_excel('EV_Vehicles_20000.xlsx', index=False)
print("✅ Vehicle dataset saved as 'EV_Vehicles_20000.xlsx'")

import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration
num_rows = 20000
start_session_id = 900001
station_id_range = (10001, 30000)
vehicle_id_range = (50001, 70000)

charging_modes = ['Fast', 'Normal', 'Trickle']
session_statuses = ['Completed', 'Interrupted', 'Scheduled']

def generate_sessions(n):
    data = []
    for i in range(n):
        session_id = start_session_id + i
        station_id = random.randint(*station_id_range)
        vehicle_id = random.randint(*vehicle_id_range)

        # Generate realistic start and end times
        start_time = datetime.strptime('2023-01-01', '%Y-%m-%d') + timedelta(minutes=random.randint(0, 1200000))
        duration_minutes = random.randint(30, 180)
        end_time = start_time + timedelta(minutes=duration_minutes)

        # Energy and payment
        energy_kwh = round(random.uniform(5, 60), 2)
        price_per_kwh = random.uniform(10, 25)
        payment_amount = round(energy_kwh * price_per_kwh, 2)

        charging_mode = random.choice(charging_modes)
        session_status = random.choice(session_statuses)

        data.append({
            'Session_ID': session_id,
            'Station_ID': station_id,
            'Vehicle_ID': vehicle_id,
            'Start_Time': start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'End_Time': end_time.strftime('%Y-%m-%d %H:%M:%S'),
            'Energy_Consumed_kWh': energy_kwh,
            'Payment_Amount': payment_amount,
            'Charging_Mode': charging_mode,
            'Session_Status': session_status
        })
    return pd.DataFrame(data)

# Generate and save
df_sessions = generate_sessions(num_rows)
df_sessions.to_excel('EV_ChargingSessions_20000.xlsx', index=False)
print("✅ Charging sessions dataset saved as 'EV_ChargingSessions_20000.xlsx'")
"""
import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration
num_rows = 20000
start_weather_id = 800001

# Reuse the same 300-location list from your stations table
locations = [
    'Delhi', 'Mumbai', 'Bengaluru', 'Hyderabad', 'Chennai', 'Kolkata', 'Pune', 'Ahmedabad', 'Jaipur', 'Lucknow',
    'Coimbatore', 'Nagpur', 'Bhopal', 'Visakhapatnam', 'Surat', 'Thane', 'Patna', 'Vadodara', 'Ghaziabad', 'Ludhiana',
    'Agra', 'Nashik', 'Faridabad', 'Meerut', 'Rajkot', 'Kalyan', 'Vasai', 'Varanasi', 'Srinagar', 'Aurangabad',
    'Dhanbad', 'Amritsar', 'Navi Mumbai', 'Allahabad', 'Ranchi', 'Howrah', 'Jabalpur', 'Gwalior', 'Vijayawada',
    'Jodhpur', 'Madurai', 'Raipur', 'Kota', 'Guwahati', 'Chandigarh', 'Solapur', 'Hubli', 'Mysuru', 'Tiruchirappalli',
    'Bareilly', 'Moradabad', 'Noida', 'Tirunelveli', 'Kollam', 'Thrissur', 'Nellore', 'Belgaum', 'Guntur', 'Warangal',
    'Salem', 'Ujjain', 'Bokaro', 'Jamshedpur', 'Dehradun', 'Ajmer', 'Jhansi', 'Kakinada', 'Panipat', 'Bathinda',
    'Shimla', 'Bilaspur', 'Rewa', 'Satna', 'Silchar', 'Siliguri', 'Aligarh', 'Rohtak', 'Hisar', 'Ambala', 'Kurukshetra',
    'Hosur', 'Pimpri-Chinchwad', 'Tirupati', 'Anantapur', 'Karimnagar', 'Nanded', 'Bhagalpur', 'Muzaffarpur',
    'Saharanpur', 'Gaya', 'Darbhanga', 'Berhampur', 'Rourkela', 'Cuttack', 'Balasore', 'Durgapur', 'Asansol',
    'Imphal', 'Aizawl', 'Gangtok', 'Shillong', 'Kohima', 'Itanagar', 'Panaji', 'Gandhinagar', 'Naya Raipur',
    'Amaravati', 'Dharwad', 'Karnal', 'Porbandar', 'Tuticorin', 'Vizhinjam', 'Mangalore', 'Kochi', 'Paradip'
]

weather_conditions = ['Clear', 'Cloudy', 'Rainy', 'Stormy', 'Foggy']

def generate_weather_data(n):
    data = []
    for i in range(n):
        weather_id = start_weather_id + i
        location = random.choice(locations)
        timestamp = datetime.strptime('2023-01-01', '%Y-%m-%d') + timedelta(minutes=random.randint(0, 1200000))
        temperature = round(random.uniform(10, 45), 1)
        rainfall = round(random.uniform(0, 100), 1)
        wind_speed = round(random.uniform(0, 40), 1)
        humidity = round(random.uniform(30, 95), 1)
        condition = random.choice(weather_conditions)

        data.append({
            'Weather_ID': weather_id,
            'Timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'Location': location,
            'Temperature_C': temperature,
            'Rainfall_mm': rainfall,
            'Wind_Speed_kph': wind_speed,
            'Humidity_pct': humidity,
            'Weather_Condition': condition
        })
    return pd.DataFrame(data)

# Generate and save
df_weather = generate_weather_data(num_rows)
df_weather.to_excel('EV_Weather_20000.xlsx', index=False)
print("✅ Weather dataset saved as 'EV_Weather_20000.xlsx'")