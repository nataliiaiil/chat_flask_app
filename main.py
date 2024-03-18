from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('Message has been received!')


@socketio.on('My event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('Received my event: ' + str(json))
    socketio.emit('My response ', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)

