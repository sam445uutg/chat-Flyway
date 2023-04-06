from flask import Flask, render_template
from  flask_socketio import SocketIO, send 

app = Flask(__name__)
app.config['SECRET'] = "secret!123"
scoket = SocketIO(app, cors_allowed_origins="*")


@scoket.on('message')
def handle_msg(message):
    print("received message:"+ message)
    if message != 'user connted!':
        send(message, broadcast=True)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    scoket.run(app,host="localhost")


