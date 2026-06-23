from scapy.all import sniff, IP

def packet_callback(packet):
    if packet.haslayer(IP):
        print("\n===== Packet Captured =====")
        print(f"Source IP      : {packet[IP].src}")
        print(f"Destination IP : {packet[IP].dst}")
        print(f"Protocol       : {packet[IP].proto}")

        try:
            payload = bytes(packet.payload)
            print(f"Payload        : {payload[:50]}")
        except:
            pass

print("Starting Network Sniffer...")
print("Capturing 10 packets...\n")

sniff(prn=packet_callback, count=10)

print("\nCapture Completed.")