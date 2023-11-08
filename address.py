import requests
import re, threading, asyncio, aiohttp, json
from datetime import datetime
from bs4 import BeautifulSoup as BS





async def address():
    test1 = datetime.now()
    if test1.strftime('%H:%M') == '14:36':
        with open('/home/akyl/shara/olt.json', "r") as file:
            a = json.load(file)
            for  b in a:
                for k, v in b.items():
                    req = requests.get(f'') # ссылка на платформу для обордований
                    soup = BS(req.text, 'lxml')
                    print(v)
                    cont = soup.find_all( "tr", class_="container")
                    for k in cont:
                        test = k.find('div', align='left')
                        mac_pon2 = test.text.splitlines()[1]
                        mac_pon = mac_pon2.replace(' ', '')
                        print(mac_pon)
                        try:
                            async with aiohttp.ClientSession() as session:
                                async with session.post(f'(ссылка на платформу для обордований)page=onu&olt={v}&mac={mac_pon}&fdb=show', timeout=0.7) as res:
                                    print(res)
                        except asyncio.exceptions.TimeoutError:
                            pass
                        except requests.exceptions.ConnectTimeout:
                            print(f'{v} че то не то')
        
while True:
    asyncio.run(address())

