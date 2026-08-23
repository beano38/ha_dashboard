import socket

# 1. Manually specify your host IP on the home network (eth1)
LOCAL_IP = "192.168.68.51" 

# Define the standard SSDP message targeting Roku devices
ssdp_message = (
    "M-SEARCH * HTTP/1.1\r\n"
    "HOST: 239.255.255.250:1900\r\n"
    'MAN: "ssdp:discover"\r\n'
    "MX: 3\r\n"
    "ST: roku:ecp\r\n" 
    "\r\n"
).encode('utf-8')

# Set up the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.settimeout(4.0)

try:
    # CRITICAL FIX: Bind the socket to your specific eth1 interface IP
    # This prevents Python from accidentally broadcasting over the 10.5.x.x link
    sock.bind((LOCAL_IP, 0))
    
    print(f"Broadcasting Roku discovery packet via interface {LOCAL_IP}...")
    sock.sendto(ssdp_message, ("239.255.255.250", 1900))
    
    discovered = False
    while True:
        try:
            data, addr = sock.recvfrom(2048)
            response = data.decode('utf-8', errors='ignore')
            
            if "roku" in response.lower():
                print(f"\n[+] SUCCESS! Found Roku Device at IP: {addr[0]}")
                # Extract location header if visible
                for line in response.split("\r\n"):
                    if line.lower().startswith("location:"):
                        print(f"    {line}")
                discovered = True
                
        except socket.timeout:
            if not discovered:
                print("\nNo Roku devices responded on this interface.")
                print("Double check if Windows Firewall is blocking inbound UDP port 1900 responses to WSL.")
            else:
                print("\nScan completed.")
            break
finally:
    sock.close()