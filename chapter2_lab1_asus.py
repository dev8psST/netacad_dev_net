import netmiko
from  netmiko  import  ConnectHandler

"""
sshCli = ConnectHandler(
    device_type = "linux",
    host = "192.168.1.1",
    port = "22",
    username = "admin",
    password = "router456"

)
"""


asus_RB12 = {
    "device_type":"linux",
    "host":"192.168.1.1",
    "port":"22",
    "username":"admin",
    "password":"router456"
}
sshCli = ConnectHandler(**asus_RB12)

output = sshCli.send_command(input(">>> "))# /version, /etc/version, busybox --list, cat /proc/cpuinfo
print(f"Command out : {output}")


