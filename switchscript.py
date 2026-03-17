import sys
from netmiko import ConnectHandler

device = {
    'device_type': 'autodetect',
    'host': '192.168.0.30',
    'username': 'ertine',
    'password': 'admin',
    'secret': 'enable',
    'port': 22,
    'conn_timeout': 16,
}
commands = ['conf t',
            'interface ethernet 0/0/3',
            'no shutdown',
            'exit', 
            'exit',
            'exit']
try:
    ssh = ConnectHandler(**device)

    output = ssh.send_command_timing('ertine')
    if 'Password' in output:
        output += ssh.send_command_timing('admin')

    output += ssh.send_command(device['secret'], expect_string=r'#')
    print("enable")

    result = ssh.send_config_set(commands)
    print (result)

except Exception as e:
    print (f"Ошибка: {e}")
