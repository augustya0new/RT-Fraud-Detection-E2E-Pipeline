from kafka import KafkaConsumer
import json
import pandas as pd

consumer = KafkaConsumer("transactions", bootstrap_servers=["localhost:9092"], value_deserializer=lambda x: json.loads(x.decode("utf-8")))

for message in consumer:
    transaction = message.value
    prediction = model.predict(pd.DataFrame([transaction]))
    if prediction[0] == 1:
        print(f"⚠️ FRAUD DETECTED: {transaction}")
