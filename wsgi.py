from flask import Flask
import os

application = Flask(__name__)

workers = os.environ.get('GUNS', 'default')
@application.route("/")
def hello():
    
    return workers

if __name__ == "__main__":
    application.run()
