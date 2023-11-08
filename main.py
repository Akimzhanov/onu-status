import json, requests, re
from datetime import datetime
from netmiko import ConnectHandler,NetMikoTimeoutException,ReadTimeout,NetmikoAuthenticationException
from paramiko.ssh_exception import SSHException
from bs4 import BeautifulSoup as BS


def format_mac(mac: str) -> str:
    mac = re.sub('[.:-]', '', mac).lower()  # remove delimiters and convert to lower case
    mac = ''.join(mac.split())  # remove whitespaces
    assert len(mac) == 12  # length should be now exactly 12 (eg. 008041aefd7e)
    assert mac.isalnum()  # should only contain letters and numbers
    # convert mac in canonical form (eg. 00:80:41:ae:fd:7e)
    mac = ":".join(["%s" % (mac[i:i+2]) for i in range(0, 12, 2)])
    return mac






while True:
    test1 = datetime.now()
    if test1.strftime('%H:%M') == '09:09':
        with open('/home/akyl/shara/olt.json', 'r') as file:
            a = json.load(file)
            t = open('/home/akyl/shara/wire_down.txt', 'w')
            t.close()
            for b in a:
                for k, v in b.items():
                    username = "" #login 
                    password = "" #password
                    port = "" #port
                    OLT = {
                        'device_type': 'cisco_ios',
                        'host': v,
                        'username': username,
                        'password': password,
                        'secret': 'secret',
                        'port': port,
                        'timeout': 30, 
                    }
                    try:
                        ssh_connect = ConnectHandler(**OLT)
                        ssh_connect.enable()
                        output = ssh_connect.send_command('terminal width 0')
                        try:
                            output3 = ssh_connect.send_command('show epon onu-info static | include wire-down', read_timeout=240, cmd_verify=False)
                            line_out = output3.splitlines()
                            hostname = ssh_connect.find_prompt()

                            f = open('/home/akyl/shara/wire_down.txt', 'a')
                            f.write(f'{hostname} - http://{v}/index.asp')
                            f.write('\n')
                            r = requests.get(f'(ссылка на платформу для обордований)?page=olt&olt={v}')
                            req = r.text

                            soup = BS(req, 'lxml')
                            cont = soup.find_all( "tr", class_="container")
                            for i in line_out:
                                mac = str(i)[37:]
                                mac2  = mac[:15]
                                try:
                                    mac3 = format_mac(mac2)
                                    mac4 = mac3.upper()
                                except AssertionError:
                                    mac4 = ''
                                for k in cont:
                                    test = k.find('div', align='left')
                                    mac_pon = test.text.splitlines()[1].strip()

                                    if mac4 == mac_pon:

                                        t = k.find_all(class_="abon_name")
                                        result = '\n'.join ('\n'.join(l) for l in t)

                                        c = str(i.replace('static', f'{result}'))

                                        f.write(c)
                                        f.write('\n')
                            f.write('\n')
                            f.write('\n')
                            f.write('\n')
                            f.close()
                                   
                        except (SSHException,ReadTimeout) as e:
                            print(f"Ошибка SSH на {v}. Invalid packet blocking: {str(e)}")
                            continue


                      
                        

                        ssh_connect.disconnect()
                        break

                    except (NetMikoTimeoutException,NetmikoAuthenticationException):
                        print(f"Ошибка подключения к {v}")

