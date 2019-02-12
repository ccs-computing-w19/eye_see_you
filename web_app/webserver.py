from flask import Flask
from main import VehicleDetect
app = Flask(__name__)

//detector = VehicleDetect()

@app.route('/')
def index():
    return 'Index Page'

# @app.route('/getData')
# def getData():
#     return str(detector.dataCapture())
