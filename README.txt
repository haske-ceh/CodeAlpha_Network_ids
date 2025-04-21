Network-Based Intrusion Detection System (NIDS) Setup

FILES INCLUDED:
1. ids_alert_visualizer.py - Python script to parse and visualize Suricata alerts
2. local.rules - A sample Suricata rule to detect ICMP packets

STEPS TO USE:
1. Install Suricata:
   sudo apt install suricata -y

2. Add 'local.rules' to /etc/suricata/rules/local.rules

3. Make sure 'local.rules' is listed in /etc/suricata/suricata.yaml under rule-files.

4. Download a test PCAP (example: icmp.pcap):
   wget https://wiki.wireshark.org/SampleCaptures?action=AttachFile&do=get&target=icmp.pcap -O icmp-test.pcap

5. Run Suricata on the PCAP:
   sudo suricata -r icmp-test.pcap -l /var/log/suricata/

6. Install matplotlib:
   pip install matplotlib

7. Run the Python script:
   python3 ids_alert_visualizer.py

This will visualize alerts like "ICMP Packet Detected".
