#!/usr/bin/env python3

import subprocess
import datetime
import os

# Directories
ARP_LOG_DIR = os.path.expanduser("~/ARP_Logs")
PING_LOG_DIR = os.path.expanduser("~/Network_Logs")
os.makedirs(ARP_LOG_DIR, exist_ok=True)
os.makedirs(PING_LOG_DIR, exist_ok=True)

# Timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Collect ARP cache
try:
    arp_output = subprocess.check_output(["arp", "-a"]).decode()
except subprocess.CalledProcessError as e:
    arp_output = f"Error executing arp command: {e}"

with open(os.path.join(ARP_LOG_DIR, f"arp_{timestamp}.log"), "w") as f:
    f.write(arp_output)

# Define ping targets
targets = ["8.8.8.8", "192.168.1.1"]  # Replace with your targets

# Ping each target
for target in targets:
    try:
        ping_output = subprocess.check_output(["ping", "-c", "4", target]).decode()
    except subprocess.CalledProcessError as e:
        ping_output = f"Error pinging {target}: {e}"

    with open(os.path.join(PING_LOG_DIR, f"ping_{target}_{timestamp}.log"), "w") as f:
        f.write(ping_output)

print(f"Data collection completed at {timestamp}")
