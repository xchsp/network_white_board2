import socket

from UserDialog import UserDialog


class Connection:
    def __init__(self):
        UserDialog.getUserInputIp()
        self.host = UserDialog._Ip
        self.port = UserDialog._port
        print(self.host,self.port)

        self.sock = socket.socket()
        self.sock.connect((self.host,self.port))



if __name__ == '__main__':
    conn = Connection()

    print('start')

