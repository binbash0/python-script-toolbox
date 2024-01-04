import socket
print(r"""
  ____                 
 |  _ \ _	_		  _         
 | |_) ( )_ __ | |	__ _  ___| |		
 |  _  - |  _ \| | _   / _` |/ __| |___		     
 | |_) | | | | |  (_) |	(_) |\__ \  _  \	     
 |____/|_|_| |_|_,___ |\__,_|_ __/ | |_|		   
""")
print(r""" ***** Network scanning tool ***** """)
def scan_ports(target, start_port, end_port):
    print(f"Scanning ports on {target}...\n")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

# Collect input from the user
target_ip = input("Enter the target IP address: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

# Perform the port scanning
scan_ports(target_ip, start_port, end_port)
