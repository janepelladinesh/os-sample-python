from flask import Flask
from kafka import KafkaConsumer
application = Flask(__name__)

@application.route("/")
def hello():
    
    return "Hello World!"

if __name__ == "__main__":
    application.run()
