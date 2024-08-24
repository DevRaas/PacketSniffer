from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # Print basic information
        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst}")
        print(f"Protocol: {protocol}")

        # Print protocol-specific details
        if TCP in packet:
            print(f"TCP Packet: Source Port: {packet[TCP].sport}, Destination Port: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"UDP Packet: Source Port: {packet[UDP].sport}, Destination Port: {packet[UDP].dport}")
        elif ICMP in packet:
            print(f"ICMP Packet: Type: {packet[ICMP].type}, Code: {packet[ICMP].code}")

        # Print payload data
        if len(packet.payload) > 0:
            payload = packet.payload.load
            print(f"Payload Data: {payload}")

        print("="*40)

def main():
    print("Starting packet sniffer...")
    # Capture packets indefinitely and call packet_callback for each packet
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
