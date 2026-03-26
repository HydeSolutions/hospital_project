from confluent_kafka import Producer
import pandas as pd
import json
import time

# -----------------------------
# Kafka configuration
# -----------------------------
conf = {
    'bootstrap.servers': 'localhost:29092',
    'client.id': 'admission-producer'
}

producer = Producer(conf)

TOPIC = "admissions-inbound"

# -----------------------------
# Delivery callback
# -----------------------------
def delivery_report(err, msg):
    if err is not None:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Sent to {msg.topic()} [{msg.partition()}] offset {msg.offset()}")

# -----------------------------
# Load CSV
# -----------------------------
df = pd.read_csv("D:\\Data_Analysis\\Projects\\hospital_project\\Kafka\\python_scripts\\admissions.csv")

# Clean column names (VERY IMPORTANT for your file)
df.columns = df.columns.str.strip()

# Ensure 1000 events
df = df.sample(n=1000, replace=True).reset_index(drop=True)

# -----------------------------
# Produce events
# -----------------------------
for i, row in df.iterrows():
    event = {
        "name": row["Name"],
        "age": int(row["Age"]),
        "gender": row["Gender"],
        "Blood Type": row["Blood Type"],
        "Medical Condition": row["Medical Condition"],
        "Date of Admission": row["Date of Admission"],
        "Doctor": row["Doctor"],
        "Hospital": row["Hospital"],
        "Insurance Provider": row["Insurance Provider"],
        "Billing Amount": float(row["Billing Amount"]),
        "Room Number": int(row["Room Number"]),
        "Admission Type": row["Admission Type"],
        "Discharge Date": row["Discharge Date"],
        "Medication": row["Medication"],
        "Test Results": row["Test Results"],
        "event_id": i,
        "timestamp": time.time()
    }

    producer.produce(
        TOPIC,
        key=str(i),
        value=json.dumps(event),
        callback=delivery_report
    )

    producer.poll(0)

    # simulate streaming
    time.sleep(0.01)

# -----------------------------
# Flush
# -----------------------------
producer.flush()

print("🚀 Finished sending 1000 hospital admission events")