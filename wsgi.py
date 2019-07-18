from flask import Flask
from kafka import KafkaConsumer
application = Flask(__name__)

@application.route("/")
def hello():
    consumer = KafkaConsumer(bootstrap_servers='victoria.com:6667',
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
    consumer.subscribe(['my-topic'])
    consumer.close()
    return "Hello World!"

if __name__ == "__main__":
    application.run()
