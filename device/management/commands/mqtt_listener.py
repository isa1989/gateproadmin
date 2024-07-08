from django.core.management.base import BaseCommand
import paho.mqtt.client as mqtt

# from your_app.models import SensorData  # SensorData modelini doğru şekilde import edin


class Command(BaseCommand):
    help = "Starts MQTT listener and saves data to Django model"

    def handle(self, *args, **options):
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code " + str(rc))
            client.subscribe("383000001/sensor/State")

        def on_message(client, userdata, msg):
            payload = msg.payload.decode()
            print(f"Received message '{payload}' on topic '{msg.topic}'")

            # SensorData.objects.create(topic=msg.topic, message=payload)

        broker_address = "46.32.168.23"
        port = 1883

        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.username_pw_set("iot", "Passw0rdIOT")

        client.connect(broker_address, port, 60)

        client.loop_forever()
