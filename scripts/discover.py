import socket

# 'ssdp:all' queries every UPnP/SSDP device on the network segment
ssdp_message = (
    "M-SEARCH * HTTP/1.1\r\n"
    "HOST: 239.255.255.250:1900\r\n"
    'MAN: "ssdp:discover"\r\n'
    "MX: 5\r\n"                  # Allow devices up to 5 seconds to respond
    "ST: ssdp:all\r\n"           # The catch-all search target
    "\r\n"
).encode('utf-8')

# Set up the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.settimeout(5.0)  # Total listen window

# Recommended: set a TTL (Time To Live) to ensure packet leaves local stack
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

try:
    print("Broadcasting generic SSDP discovery packet to network...")
    sock.sendto(ssdp_message, ("239.255.255.250", 1900))
    
    discovered_ips = set()
    
    while True:
        try:
            data, addr = sock.recvfrom(2048)
            response = data.decode('utf-8', errors='ignore')
            
            # Print unique discoveries to keep terminal clean
            if addr[0] not in discovered_ips:
                discovered_ips.add(addr[0])
                print(f"\n========================================")
                print(f"[+] DISCOVERED DEVICE AT IP: {addr[0]}")
                print(f"========================================")
                
            # Print the raw headers returned by the device
            print(response.strip())
            
        except socket.timeout:
            print(f"\nScan finished. Total unique devices found: {len(discovered_ips)}")
            break
finally:
    sock.close()