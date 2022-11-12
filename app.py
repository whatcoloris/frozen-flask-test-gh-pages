import sys,os
from flask import Flask
from flask_frozen import Freezer
#from dotenv import load_dotenv
#load_dotenv()

app = Flask(__name__)

freezer = Freezer(app)

@app.route("/")
def index():
    return "Hello World!!"

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)