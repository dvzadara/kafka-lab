from websockets.sync.client import connect
import json
import time

from kafka import KafkaConsumer


if __name__ == '__main__':
    consumer = KafkaConsumer("bitcoin", auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
    maximums = []
    n = 0
    for msg in consumer:
        time.sleep(0.1)
        record = json.loads(msg.value)
        price = float(record["data"]['price'])
        maximums.append(price)
        maximums.sort(reverse=True)
        maximums = maximums[:10]
        print(maximums)
        n += 1
    if consumer is not None:
        consumer.close()
    print("10 max prices:")
    print(maximums)
    print(f"Number of prices: {n}")