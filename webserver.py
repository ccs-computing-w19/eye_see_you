from flask import Flask
from main import VehicleDetect
app = Flask(__name__)

detector = VehicleDetect()

@app.route('/')
def index():
    return 'Index Page'

@app.route('/getData')
def hello():
    return str(detector.dataCapture())

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath