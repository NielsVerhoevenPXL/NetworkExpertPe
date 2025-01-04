from netmiko import ConnectHandler
import time
import os

# Router configuration dictionary
router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "port": 22,  # Default SSH port
    "username": "cisco",
    "password": "cisco123!"
}

# Threshold for bandwidth utilization (in percentage)
BANDWIDTH_THRESHOLD = 80

# Log file path
LOG_FILE = "outputs/interface_status_log.txt"

# Function to get router connection
def get_router_connection(router_config):
    return ConnectHandler(**router_config)

# Function to check interface status and bandwidth utilization
def check_interface_status(connection):
    interfaces_status = connection.send_command("show ip interface brief")
    interfaces = interfaces_status.splitlines()[1:]

    alerts = []

    for interface in interfaces:
        details = interface.split()
        if len(details) < 6:
            continue

        intf_name = details[0]
        intf_status = details[4]
        intf_protocol = details[5]

        if intf_status != "up" or intf_protocol != "up":
            alerts.append(f"ALERT: {intf_name} is down (Status: {intf_status}, Protocol: {intf_protocol})")

        bandwidth_utilization = connection.send_command(f"show interfaces {intf_name} | include rate")
        if "input rate" in bandwidth_utilization and "output rate" in bandwidth_utilization:
            input_rate = int(bandwidth_utilization.split("input rate")[1].split()[0])
            output_rate = int(bandwidth_utilization.split("output rate")[1].split()[0])
            total_rate = input_rate + output_rate

            if total_rate > BANDWIDTH_THRESHOLD:
                alerts.append(f"ALERT: {intf_name} bandwidth utilization is high (Input: {input_rate}%, Output: {output_rate}%)")

    return interfaces_status, alerts

# Function to log interface status and alerts
def log_status_and_alerts(status, alerts):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        log_file.write(status)
        log_file.write("\n" + "="*50 + "\n")
        for alert in alerts:
            log_file.write(alert + "\n")
        log_file.write("\n" + "="*50 + "\n")

# Main function
def main():
    # Ensure the outputs directory exists
    os.makedirs("outputs", exist_ok=True)

    # Establish SSH connection to the router
    net_connect = get_router_connection(router)

    while True:
        # Check interface status and bandwidth utilization
        status, alerts = check_interface_status(net_connect)

        # Log status and alerts
        log_status_and_alerts(status, alerts)

        # Print alerts to console
        for alert in alerts:
            print(alert)

        # Wait for 5 minutes before the next check
        time.sleep(300)

if __name__ == "__main__":
    main()