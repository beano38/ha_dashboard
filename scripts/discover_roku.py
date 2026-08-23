from roku import Roku

print("Scanning local network for Roku devices...")
# Discover all Roku devices on the local subnet
devices = Roku.discover()

if not devices:
    print("No Roku devices found. Check your Wi-Fi network.")
else:
    for device in devices:
        # Prints the device object containing the IP address and port
        print(f"Found Roku at: http://{device.host}:{device.port}")
        