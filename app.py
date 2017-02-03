import os
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    application.run(host=os.environ['DEV_SERVICE_HOST'],
        port=os.environ['DEV_SERVICE_PORT'])
