import socket

def scan_ports(target: str, start_port: int, end_port: int):
    open_ports = []

    print(f"Scanning {target} from port {start_port} to {end_port}")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        sock.close()

    print("Scan complete")

    return open_ports