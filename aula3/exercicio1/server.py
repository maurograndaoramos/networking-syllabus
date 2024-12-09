import socket
import time

HOST = "0.0.0.0"
PORT = 8080
IDLE_TIMEOUT = 32

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    print(f"Listening on {HOST}:{PORT}", flush=True)
    server.listen(2)

    while True:
        conn, address = server.accept()
        print(f"Connected by {address}", flush=True)
        conn.sendall(b"Connected, please wait for authentication...")
        time.sleep(2)

        attempts = 3

        authenticated = False
        while attempts > 0:
            print(f"Requesting {address} for password", flush=True)
            conn.sendall(b" Please provide password:")

            password = conn.recv(1024).decode().strip()

            if password == "GiveMeADecentGrade":
                authenticated = True
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"{address} provided wrong password, {attempts} attempts left.", flush=True)
                    conn.sendall(b"Wrong password, try again.")
                else:
                    print(f"{address} exceeded attempts, closing connection.", flush=True)
                    conn.sendall(b"Too many attempts, closing connection.")
                    conn.close()

        if authenticated:
            with conn:
                conn.sendall(b"Welcome to ETIC Socket Server! You are now authenticated. Type something here: ")
                conn.settimeout(IDLE_TIMEOUT)

                while True:
                    try:
                        data = conn.recv(1024)
                        if not data:
                            print(f"{address} shutting connection down.", flush=True)
                            break
                        print(f"Received: {data.decode()}", flush=True)
                        conn.sendall(b"Here's what you sent, buddy: " + data)
                    except socket.timeout:
                        print(f"{address} timed out, closing connection.", flush=True)
                        conn.sendall(b"Connection timed out, shutting you out! ")
                        break