import json
import os
import matplotlib.pyplot as plt
from collections import Counter

LOG_FILE = "/var/log/suricata/eve.json"

def check_log_file():
    if not os.path.exists(LOG_FILE):
        print(f"[!] Log file not found: {LOG_FILE}")
        return False
    return True

def parse_alerts():
    alert_counts = Counter()
    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if "alert" in data:
                        msg = data["alert"]["signature"]
                        alert_counts[msg] += 1
                except json.JSONDecodeError:
                    continue
    except Exception as e:
        print(f"[!] Error reading log file: {e}")
        return alert_counts
    return alert_counts

def visualize_alerts(alert_counts):
    if not alert_counts:
        print("[!] No alerts found to visualize.")
        return

    labels, values = zip(*alert_counts.items())
    plt.figure(figsize=(10, 6))
    plt.barh(labels, values, color='skyblue')
    plt.xlabel("Alert Count")
    plt.title("Suricata Intrusion Alerts")
    plt.tight_layout()
    plt.grid(True, axis='x', linestyle='--', alpha=0.5)
    plt.show()

def main():
    print("[*] Network-Based IDS Alert Visualizer")
    if not check_log_file():
        return
    alerts = parse_alerts()
    print(f"[+] Found {sum(alerts.values())} alert(s) across {len(alerts)} type(s).")
    for alert, count in alerts.items():
        print(f"  - {alert}: {count}")
    visualize_alerts(alerts)

if __name__ == "__main__":
    main()
