#!/usr/bin/env python3
import socket

target = input("🔍 Ingrese la IP o dominio a escanear: ")
ports = [21, 22, 80, 443, 8080]

print(f"Escaneando {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"✅ Puerto {port} abierto")
