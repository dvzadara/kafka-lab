from websockets.sync.client import connect
import json
import time

from kafka import KafkaProducer


def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer


server_ip = "wss://ws.bitstamp.net"

channgel_name = "live_orders_btcusd"

subscription_msg = {
    "event": "bts:subscribe",
    "data": {
        "channel": channgel_name
    }
}

unsubscription_msg = {
    "event": "bts:unsubscribe",
    "data": {
        "channel": channgel_name
    }
}

if __name__ == '__main__':
    with connect(server_ip) as websocket:
        topic_name = "test"
        websocket.send(json.dumps(subscription_msg))
        message = websocket.recv()
        print(f"Received: {message}")

        print("-" * 20)
        kafka_producer = connect_kafka_producer()

        for _ in range(30):
            time.sleep(0.1)
            message = websocket.recv()
            print(f"Received: {message}")
            publish_message(kafka_producer, 'bitcoin', 'raw', message)
        print("-" * 20)
        if kafka_producer is not None:
            kafka_producer.close()

        websocket.send(json.dumps(unsubscription_msg))