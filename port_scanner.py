import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    """
    Scans a specific port on the target IP address.

    :param target: Target IP address
    :param port: Port number to scan
    :return: A string indicating whether the port is open or closed
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout for each port scan
            result = s.connect_ex((target, port))  # Attempt connection
            if result == 0:
                return f"Port {port}: OPEN"
    except Exception as e:
        return f"Port {port}: ERROR ({e})"
    return f"Port {port}: CLOSED"


def main():
    print("Welcome to Port Scanner!")
    target = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    
    with ThreadPoolExecutor(max_workers=10) as executor:  # Multithreaded scanning
        futures = [executor.submit(scan_port, target, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            print(future.result())

    print("\nScan complete!")


if __name__ == "__main__":
    main()

