from flask import Flask
from kafka import KafkaConsumer
application = Flask(__name__)

@application.route("/")
def hello():
    consumer = KafkaConsumer(bootstrap_servers='10.128.0.202:9092',
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
    consumer.subscribe(['test'])
    consumer.close()
    return "Hello World!"

if __name__ == "__main__":
    application.run()
