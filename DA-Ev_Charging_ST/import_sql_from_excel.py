import csv
import mysql.connector

# ✅ Step 1: Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0909',
    database='Ev_charging'
)
cursor = conn.cursor()

# ✅ Step 2: Open CSV and insert rows
with open(r"C:\Users\ADMIN\OneDrive\Desktop\DA-Ev_Charging_ST\EV_Weather.csv", mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row

    for row in csv_reader:
        cursor.execute("""
            INSERT IGNORE INTO weather ( Weather_ID,Timestamp,Location,Temperature_C,Rainfall_mm,Wind_Speed_kph,Humidity_pct,Weather_Condition)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, row)

# ✅ Step 3: Commit and close
conn.commit()
cursor.close()
conn.close()
print("✅ Data inserted successfully into 'weather' table (duplicates ignored).")