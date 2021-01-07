import logging
import socket

log = logging.getLogger('proxy')


class HealthCheck:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def check_instance(self):
        open_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        open_socket.settimeout(3)
        endpoint = (self.host, self.port)
        result_of_check = open_socket.connect_ex(endpoint)
        if result_of_check == 0:
            return True
        log.warning('Instance {} port {} is DOWN'.format(self.host, self.port))
        return False
