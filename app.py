# #Setting up Flask pre-class 9.4.3
# Import dependencies
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'