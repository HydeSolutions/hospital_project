from kafka import KafkaConsumer
import json
import pandas as pd
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values

import time

# -----------------------------
# Kafka Consumer
# -----------------------------
consumer = KafkaConsumer(
    'admissions-inbound',
    bootstrap_servers='localhost:29092',
    auto_offset_reset='latest',      # or 'latest'
    enable_auto_commit=True,
    group_id='hospital-loader',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# -----------------------------
# Postgres connection
# -----------------------------
conn = psycopg2.connect(
    host="localhost",
    database="hospital_project",   # change this
    user="ali",
    password="ali@123"
)
cur = conn.cursor()

# # Create table once (or run this manually in psql)
# create_table_sql = """
# CREATE TABLE IF NOT EXISTS main (
#     event_id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER,
#     gender TEXT,
#     "Blood Type" TEXT,
#     "Medical Condition" TEXT,
#     Doctor TEXT,
#     hospital TEXT,
#     "Insurance Provider" TEXT,
#     "Billing Amount" NUMERIC,
#     "Room Number" INTEGER,
#     "Admission Type" TEXT,
#     Medication TEXT,
#     "Test Results" TEXT,
#     "Date of Admission" TIMESTAMP,
#     "Discharge Date" TIMESTAMP,
# );
# """
# cur.execute(create_table_sql)
# conn.commit()

print("Listening for messages... Press Ctrl+C to stop")

batch = []
BATCH_SIZE = 1000   # adjust based on your volume

try:
    for message in consumer:
        event = message.value
        batch.append(event)
        
        if len(batch) >= BATCH_SIZE:
            df = pd.DataFrame(batch)
            df["Date of Admission"] = pd.to_datetime(df["Date of Admission"], dayfirst=True)
            df["Discharge Date"] = pd.to_datetime(df["Discharge Date"], dayfirst=True)

            cols = list(df.columns)
            values = [tuple(x) for x in df.to_numpy()]

            query = sql.SQL("""
                INSERT INTO main ({fields})
                VALUES %s
                ON CONFLICT ("Date of Admission") DO NOTHING
            """).format(
                fields=sql.SQL(',').join(map(sql.Identifier, cols))
            )

            execute_values(cur, query.as_string(conn), values)
            conn.commit()
            
            print(f"✅ Inserted batch of {len(batch)} records")
            batch = []

except KeyboardInterrupt:
    print("Stopping consumer...")
except Exception as e:
    conn.rollback()
    print("Error:", e)
finally:
    if batch:  # insert remaining records
        df = pd.DataFrame(batch)
        tuples = [tuple(x) for x in df.to_numpy()]
        # cols = ','.join(df.columns)
        # query = f"INSERT INTO main ({cols}) VALUES %s ON CONFLICT (event_id) DO NOTHING"
        # execute_values(cur, query, tuples)
        # conn.commit()
        cols = list(df.columns)
        values = [tuple(x) for x in df.to_numpy()]

        query = sql.SQL("""
            INSERT INTO main ({fields})
            VALUES %s
            ON CONFLICT ("event_id") DO NOTHING
        """).format(
            fields=sql.SQL(',').join(map(sql.Identifier, cols))
        )

        execute_values(cur, query.as_string(conn), values)
        conn.commit()
    
    cur.close()
    conn.close()
    consumer.close()