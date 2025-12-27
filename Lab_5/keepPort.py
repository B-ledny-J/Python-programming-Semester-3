import socket
import threading

ports = [21, 22, 23, 25, 53, 80, 110, 143]

def listen(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", port))
    s.listen(1)
    print(f"Listening on port {port}")
    while True:
        conn, addr = s.accept()
        conn.close()

for p in ports:
    threading.Thread(target=listen, args=(p,), daemon=True).start()

input("Press Enter to stop...\n")
