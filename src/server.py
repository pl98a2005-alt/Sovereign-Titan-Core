import socket, threading, json
class GameServer:
    def __init__(self, host='0.0.0.0', port=5000):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(10)
    def start(self):
        print("[Sovereign Server Online]")
        while True:
            c, a = self.s.accept()
            threading.Thread(target=lambda: c.recv(1024)).start()
if __name__ == "__main__": GameServer().start()

