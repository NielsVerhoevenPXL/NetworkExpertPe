from netmiko import ConnectHandler
from pprint import pprint
import os

def get_router_connection(router_config):
    return ConnectHandler(**router_config)

def read_config_file(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()

def send_config_commands(connection, commands):
    try:
        return connection.send_config_set(commands)
    except Exception as e:
        print(f"Error sending config commands: {e}")
        return None

def run_show_commands(connection, commands):
    outputs = {}
    for command in commands:
        try:
            outputs[command] = connection.send_command(command)
        except Exception as e:
            print(f"Error running show command '{command}': {e}")
            outputs[command] = None
    return outputs

def save_output_to_file(file_path, outputs):
    with open(file_path, "w") as file:
        for command, output in outputs.items():
            file.write(f"Command: {command}\n")
            file.write(output if output else "Error retrieving output")
            file.write("\n" + "="*50 + "\n")

def backup_device_config(connection, backup_file_path):
    try:
        backup_output = connection.send_command("show running-config")
        with open(backup_file_path, "w") as backup_file:
            backup_file.write(backup_output)
    except Exception as e:
        print(f"Error backing up device config: {e}")

def configure_router(router):
    try:
        # Establish SSH connection to the router
        net_connect = get_router_connection(router)

        # Local configuration commands
        local_config_commands = [
            "hostname CSR1000v_Local"
        ]

        # Read configuration commands from external file
        external_config_commands = read_config_file("config_script.txt")

        # Combine local and external configuration commands
        config_commands = local_config_commands + external_config_commands

        # Send configuration commands
        config_output = send_config_commands(net_connect, config_commands)
        print(f"Configuration Output for {router['host']}:\n")
        pprint(config_output)
        print("\n" + "="*50 + "\n")

        # Check if subinterfaces are already configured
        subinterface_check_commands = [
            "show run int GigabitEthernet1.10",
            "show run int GigabitEthernet1.20"
        ]
        subinterface_check_output = run_show_commands(net_connect, subinterface_check_commands)

        if "Invalid input detected" in subinterface_check_output["show run int GigabitEthernet1.10"]:
            print("Configuring subinterfaces...")
            # Configure subinterfaces
            subinterface_config_commands = [
                "interface GigabitEthernet1.10",
                "encapsulation dot1Q 10",
                "ip address 192.168.10.1 255.255.255.0",
                "no shutdown",
                "interface GigabitEthernet1.20",
                "encapsulation dot1Q 20",
                "ip address 192.168.20.1 255.255.255.0",
                "no shutdown"
            ]

            subinterface_config_output = send_config_commands(net_connect, subinterface_config_commands)
            print("Subinterface Configuration Output:\n")
            pprint(subinterface_config_output)
            print("\n" + "="*50 + "\n")
        else:
            print("Subinterfaces are already configured. Skipping configuration.")

        # Run some show commands
        show_commands = [
            "show run int GigabitEthernet1.10",
            "show run int GigabitEthernet1.20",
            "show ip route",
            "show version"
        ]

        show_outputs = run_show_commands(net_connect, show_commands)

        # Ensure the outputs directory exists
        os.makedirs("outputs", exist_ok=True)

        # Save the output to a file
        save_output_to_file(f"outputs/show_outputs_{router['host']}.txt", show_outputs)

        # Backup the device configuration
        backup_device_config(net_connect, f"outputs/csr1000v_backup_{router['host']}")

        print(f"Backup completed successfully for {router['host']}.")
    except Exception as e:
        print(f"Error configuring router {router['host']}: {e}")

def main():
    # Router configuration dictionaries
    routers = [
        {
            "device_type": "cisco_ios",
            "host": "192.168.56.101",
            "port": 22,  # Default SSH port
            "username": "cisco",
            "password": "cisco123!"
        },
        {
            "device_type": "cisco_ios",
            "host": "192.168.56.102",
            "port": 22,  # Default SSH port
            "username": "cisco",
            "password": "cisco123!"
        }
    ]

    for router in routers:
        configure_router(router)

if __name__ == "__main__":
    main()