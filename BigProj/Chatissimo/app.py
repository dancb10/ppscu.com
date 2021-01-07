from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

from flask_socketio import join_room, leave_room
from flask_socketio import send, emit


@socketio.on('my event')
def handle_my_custom_event(data):
    emit('my response', data, broadcast=True)

@socketio.on('message')
def handle_message(message):
    send(message, namespace='/chat')

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
