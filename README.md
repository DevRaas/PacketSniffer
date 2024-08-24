# Packet Sniffer

**Packet Sniffer** is a simple Python tool designed to capture and analyze network packets. This tool displays relevant information such as source and destination IP addresses, protocols, and payload data.

**Note:** This project is intended for educational purposes only. Ensure you have explicit permission to use this sniffer and comply with all legal and ethical guidelines.

## Features

- **Packet Capture**: Captures network packets in real-time.
- **Information Display**: Shows source and destination IP addresses, protocols, and payload data.

## Installation

### Prerequisites

Make sure you have Python 3.x installed on your machine.

### Install Required Libraries

Install the `scapy` library using pip:

```bash
pip install scapy
```

## Usage

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/DevRaas/PacketSniffer.git
   cd PacketSniffer
   ```

2. **Run the Script**

   Execute the packet sniffer script with administrative privileges:

   ```bash
   sudo python packet_sniffer.py
   ```

   On Windows, run the command prompt as an administrator.

### Example Output

```
Starting packet sniffer...
Source IP: 192.168.1.1 -> Destination IP: 192.168.1.2
Protocol: 6
TCP Packet: Source Port: 12345, Destination Port: 80
Payload Data: b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'
========================================
```

## Important Considerations

- **Ethical Use**: This tool should only be used with explicit permission on networks you own or have authorization to monitor. Unauthorized packet sniffing is illegal and unethical.
- **Administrative Privileges**: Packet sniffing typically requires administrative or root access.
- **Privacy**: Handle captured data responsibly and comply with privacy laws.

## Disclaimer

**Use of this packet sniffer tool is at your own risk.** The creators of this tool are not responsible for any misuse or legal consequences arising from its use. Always ensure you have proper authorization and respect all applicable laws and regulations.

## Contributing

Contributions are welcome. To contribute to the project:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## Contact

For questions or feedback, please contact [roshanajith7911@gmail.com](mailto:roshanajith7911@gmail.com).

## Acknowledgements

- Thanks to the `scapy` library for packet capturing and analysis.
