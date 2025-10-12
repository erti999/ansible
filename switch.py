from netmiko import ConnectHandler

device = {
    'device_type': 'autodetect',
    'host': '172.16.6.244',
    'username': 'ertine',
    'password': 'admin',
    'secret': 'enable',
    'port': 22,
    'conn_timeout': 16,
    'session_log': 'log.txt',
}

commands = ['conf t',
            'interface ethernet 0/0/3',
            'shutdown',
            'exit']

try:
    ssh = ConnectHandler(**device)

    output = ssh.send_command_timing('ertine')
    if 'Password' in output:
        output += ssh.send_command_timing('admin')

    output += ssh.send_command(device['secret'], expect_string=r'#')
    print("enable")

    result = ssh.send_config_set(commands)
    print(result)

except Exception as e:
    print(f"Ошибка: {e}")