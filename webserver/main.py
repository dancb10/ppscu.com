import socket
import sys


class Ppscuweb(object):

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    socket_backlog = 100

    def __init__(self, port=80, hostname="localhost"):
        self.port = port
        if hostname:
            self.hostname = hostname
        else:
            self.hostname = socket.gethostname()

        self.listening_socket = listening_socket = socket.socket(
          self.address_family,
          self.socket_type
        )

        self.listening_socket.bind((self.hostname,self.port))
        self.listening_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listening_socket.listen(self.socket_backlog)

    def close_socket(self):
        pass

    def run_server(self):
        listening_socket = self.listening_socket
        try:
            while True:
                newconnection, conn = listening_socket.accept()
                msg = newconnection.recv(4096)
                print(msg[0])

                newconnection.send(("""### You are connected to {0} on port {1} ### \n""").format(socket.gethostname(), self.port))
        finally:
            listening_socket.close()

if __name__ == '__main__':
    SERVER_PORT = 8080
    HOSTNAME = "localhost"
    myserver = Ppscuweb(SERVER_PORT,HOSTNAME)
    print("Listening on port {0} on {1}".format(str(SERVER_PORT), HOSTNAME))
    myserver.run_server()
