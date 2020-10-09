from celery_config.celery import celery_app
from kafka import KafkaConsumer
from json import loads
import requests
import globals


url = "http://0.0.0.0:7000/update_state/"


@celery_app.task()
def consume(topic):
    topic = topic + "_d"
    print(f"topic name : {topic}")
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=[globals.KAFKA_HOSTNAME + ':' + globals.KAFKA_PORT],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="my-group",
        value_deserializer=lambda x: loads(x.decode("utf-8")),
        security_protocol="SASL_PLAINTEXT",
        sasl_mechanism='PLAIN',
        sasl_plain_username=globals.KAFKA_USERNAME,
        sasl_plain_password=globals.KAFKA_PASSWORD
    )
    for message in consumer:
        message = message.value
        print(message)
        payload = {
            "topic_name": topic,
            "value": str(message),
            "CLIENT_ID": globals.CLIENT_ID
        }

        requests.request("POST", url, data=payload)
