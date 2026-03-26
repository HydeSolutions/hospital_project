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
df = pd.read_csv("D:\\Data_Analysis\\Projects\\hospital_project\\Kafka\\admissions.csv")

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
        "blood_type": row["Blood Type"],
        "medical_condition": row["Medical Condition"],
        "date_of_admission": row["Date of Admission"],
        "doctor": row["Doctor"],
        "hospital": row["Hospital"],
        "insurance_provider": row["Insurance Provider"],
        "billing_amount": float(row["Billing Amount"]),
        "room_number": int(row["Room Number"]),
        "admission_type": row["Admission Type"],
        "discharge_date": row["Discharge Date"],
        "medication": row["Medication"],
        "test_results": row["Test Results"],
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