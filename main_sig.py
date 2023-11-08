import requests, json
import asyncio as AS
from datetime import datetime
from bs4 import BeautifulSoup as BS


async def testy():
    test1 = datetime.now()
    if test1.strftime('%H:%M') == '04:04':
        with open('/home/akyl/shara/olt.json', 'r') as file:
            a = json.load(file)
            f = open('/home/akyl/shara/address.txt', 'w')
            f.close()
            for  b in a:
                for k, v in b.items():
                    req = requests.get(f'(ссылка на платформу для обордований)?page=olt&olt={v}')
                    soup = BS(req.text, 'lxml')
                    print(v)
                    f = open('/home/akyl/shara/address.txt', 'a')
                    f.write(f'http://{v}/index.asp')
                    f.write('\n')

                    cont = soup.find_all( "tr", class_="container")
                    for k in cont:

                        test = k.find('td', style="padding:0px;")
                        test2 = test.find('font')
                        address2 = k.find('td', class_="abon_name")
                        address = str(address2)[22:-5]

                        por = k.find('div').find('font').find('b')
                        port= str(por)[3:-4]

                        if test2 != None:
                            signal = str(test2)[18:23]
                            try:
                                a = abs(float(signal))
                                addr = len(address)
                                if a >=27.0 and addr != 0:
                                    signal2 = a
                                    test = f'{address}      {port}      -{signal2}'
                                    f.write(test)
                                    f.write('\n')
                            except ValueError:
                                pass
                        else:
                            signal = str(test)[25:30]
                            try:
                                addr = len(address)
                                a = abs(float(signal))
                                if a >=27.0 and addr != 0:
                                    signal2 = a
                                    test = f'{address}      {port}      -{signal2}'
                                    f.write(test)
                                    f.write('\n')
                            except ValueError:
                                pass                            
                    f.write('\n')
                    f.write('\n')
                    f.close()

while True:
    AS.run(testy())

