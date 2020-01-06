import socket
import time

from UserDialog import UserDialog


class Connection:
    def __init__(self):
        UserDialog.getUserInputIp()
        self.host = UserDialog._Ip
        self.port = UserDialog._port
        print(self.host,self.port)

        self.sock = socket.socket()
        self.sock.connect((self.host,self.port))
        data = self.sock.recv(3).decode()
        print(data)

        UserDialog.getUserNickName()
        self.nickname = UserDialog._nickname

        self.sock.sendall((self.nickname.encode('utf-8')))

    def start(self):
        while True:
            time.sleep(0.1)
            pass

if __name__ == '__main__':
    conn = Connection()
    conn.start()
    print('start')

