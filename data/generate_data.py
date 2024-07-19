import json
import random
from datetime import datetime, timedelta

# Constants for the types of data points
NETWORK_LOG = "network_log"
IDS_ALERT = "ids_alert"
AUTH_RECORD = "auth_record"

# Generate a random IP address
def generate_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

# Generate a random timestamp within the last 24 hours
def generate_timestamp():
    return (datetime.now() - timedelta(minutes=random.randint(0, 1440))).isoformat()

# Generate a consistent data structure for network log
def generate_network_log():
    return {
        "type": NETWORK_LOG,
        "timestamp": generate_timestamp(),
        "source_ip": generate_ip(),
        "destination_ip": generate_ip(),
        "bytes_sent": random.randint(1, 65535),
        "protocol": random.choice(["TCP", "UDP", "ICMP"]),
        "flag": random.choice(["SYN", "ACK", "RST", "FIN"])
    }

# Generate a consistent data structure for IDS alert
def generate_ids_alert():
    return {
        "type": IDS_ALERT,
        "timestamp": generate_timestamp(),
        "source_ip": generate_ip(),
        "alert_type": random.choice(["Malware", "Unauthorized Access", "DDoS", "Data Leak"]),
        "severity": random.choice(["Low", "Medium", "High"])
    }

# Generate a consistent data structure for authentication record
def generate_auth_record():
    return {
        "type": AUTH_RECORD,
        "timestamp": generate_timestamp(),
        "user": f"user{random.randint(1, 100)}",
        "auth_method": random.choice(["Password", "Biometrics", "Token"]),
        "success": random.choice([True, False])
    }

# Generate the dummy data with consistent structure for each type
def generate_dummy_data(file_path, num_records=1000):
    with open(file_path, 'w') as file:
        for _ in range(num_records // 3):
            # Generate and write network log data
            network_log = generate_network_log()
            file.write(json.dumps(network_log) + "\n")

            # Generate and write IDS alert data
            ids_alert = generate_ids_alert()
            file.write(json.dumps(ids_alert) + "\n")

            # Generate and write authentication record data
            auth_record = generate_auth_record()
            file.write(json.dumps(auth_record) + "\n")

# Specify the file path and generate the data
file_path = './security_analytics_data.json'
generate_dummy_data(file_path)

# Return the path of the generated file
file_path