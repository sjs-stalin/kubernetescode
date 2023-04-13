from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'One touch app build using devops on EKS TY!!! *****************Thanks**************'
