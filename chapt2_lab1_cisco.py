import netmiko
from  netmiko  import  ConnectHandler

"""
sshCli = ConnectHandler(
    device_type = "cisco_ios",
    host = "localhost",
    port = "5022",
    username = "cisco",
    password = "cisco123!"

)
"""
cisco_router_1 = {
    "device_type": "cisco_ios",
    "host": "localhost",
    "port": "5022",
    "username": "cisco",
    "password": "cisco123!"
}

sshCli =  ConnectHandler(**cisco_router_1)
sshCli.enable()

output = sshCli.send_command("sh ip int br")
print(f"Command out : {output}")

config_command_1 = [
    "int loopback 1",
    "ip add 1.1.1.1 255.255.255.0",
    "description This int was configured with netmiko"
]

config_command_2 = [
    "int GigabitEthernet 1",
    "ip add 192.168.0.1 255.255.255.0",
    "description LAN to PC-B",
    "no shutdown"
]

output_set = sshCli.send_config_set(config_command_1)
#print(f"Send command : {output_set}")

sshCli.exit_enable_mode()
sshCli.disconnect()

