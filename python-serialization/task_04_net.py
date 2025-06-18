#!/usr/bin/env python3
import socket
import json

HOST = '127.0.0.1'  # localhost
PORT = 65432        # non-privileged port

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((HOST, PORT))
        server_sock.listen(1)
        conn, addr = server_sock.accept()
        with conn:
            data = b""
            while True:
                packet = conn.recv(4096)
                if not packet:
                    break
                data += packet
            try:
                received_dict = json.loads(data.decode('utf-8'))
                print("Received Dictionary from Client:")
                print(received_dict)
            except json.JSONDecodeError:
                print("Failed to decode JSON data")

def send_data(data_dict):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
            client_sock.connect((HOST, PORT))
            serialized = json.dumps(data_dict).encode('utf-8')
            client_sock.sendall(serialized)
    except Exception as e:
        print(f"Error sending data: {e}")

