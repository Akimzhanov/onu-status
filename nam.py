from fast_bitrix24 import BitrixAsync
import requests
import asyncio, time
from datetime import date, timedelta

async def count_podkl(count_abon):
    token_bot = 'TOKEN'
    url = f'api telegram'
    tg_id1 = ''
    tg_id2 = ''
    tg_id3 = ''
    tg_id4 = ''
    tg_id5 = ''
    tg_id6 = ''

    chat_ids = [tg_id1, tg_id2, tg_id3, tg_id4, tg_id5, tg_id6]
    results = []

    for chat_id in chat_ids:
        params = {
            'chat_id': chat_id,
            'text': f'Всего подключений {count_abon}'
        }
        response = requests.post(url, params)
        results.append(response)
    

    return results

async def testik(region, c):
    token_bot = 'TOKEN'
    url = f'api telegram'
    tg_id1 = ''
    tg_id2 = ''
    tg_id3 = ''
    tg_id4 = ''
    tg_id5 = ''
    tg_id6 = ''
    chat_ids = [tg_id1, tg_id2, tg_id3, tg_id4, tg_id5,tg_id6]
    results = []

    for chat_id in chat_ids:
        params = {
            'chat_id': chat_id,
            'text': f'{region}: {c} новых подключений'
        }
        response = requests.post(url, params)
        results.append(response)

    return results

async def paramss(last_day1,category_id,stage_id2):
    params = {
    'filter': {
        '>=UF_CRM_1678857157479': last_day1.replace(day=1).isoformat(),  # Начало периода (предыдущий день)
        '<=UF_CRM_1678857157479': last_day1.isoformat(),
        'CATEGORY_ID': category_id,                  # Фильтр по категории "Жалобы абонентов"
        'STAGE_ID': stage_id2
    },
    'select': ['ID'],
    'start': 0,
}
    return params

async def podkl():
    test1 = time.strftime('%H:%M')
    if test1 == '09:40':
        webhook = "" # токен с битрикс24
        b = BitrixAsync(webhook)
        
        # Получить текущую дату
        today1 = date.today()
        last_day1 = today1 - timedelta(days=1)
        testy = {23: 'C23:UC_K58IZI', 29: 'C29:5', 30: 'C30:5', 31: 'C31:5', 32: 'C32:5', 33: 'C33:5'}
        count_abon = 0
        for category_id, stage_id in testy.items():
            print(last_day1.replace(day=1).isoformat())
            print(last_day1.isoformat())
            method = 'crm.deal.list'
            if stage_id == 'C23:UC_K58IZI':
                stage_id2 = [stage_id,'C23:WON', 'C23:UC_HMWLZ7','C23:UC_PGKG8D', 'C23:UC_WN8CY1', 'C23:UC_NSYVVS', 'C23:UC_T3AU56', 'C23:UC_ZT3TE0']   
                params = await paramss(last_day1,category_id,stage_id2)
            elif stage_id == 'C29:5':
                stage_id2 = [stage_id,'C29:WON', 'C29:UC_M62DQM', 'C29:UC_90FBRQ', 'C29:UC_7LUGXR', 'C29:UC_UWHSW9', 'C29:UC_FCJXD8', 'C29:UC_M0T0LD']
                params = await paramss(last_day1,category_id,stage_id2)
            elif stage_id == 'C30:5':
                stage_id2 = [stage_id,'C30:WON', 'C30:6', 'C30:7', 'C30:8', 'C30:9', 'C30:10',' C30:11']
                params = await paramss(last_day1,category_id,stage_id2)
            elif stage_id == 'C31:5':
                stage_id2 = [stage_id,'C31:WON', 'C31:6', 'C31:UC_74X17L', 'C31:7', 'C31:9', 'C31:8', 'C31:10']
                params = await paramss(last_day1,category_id,stage_id2)
            elif stage_id == 'C32:5':
                stage_id2 = [stage_id,'C32:WON', 'C32:11', 'C32:6', 'C32:7', 'C32:8', 'C32:9', 'C32:10']
                params = await paramss(last_day1,category_id,stage_id2)
            elif stage_id == 'C33:5':
                stage_id2 = [stage_id,'C33:WON', 'C33:6', 'C33:7', 'C33:8', 'C33:9', 'C33:10', 'C33:11']
                params = await paramss(last_day1,category_id,stage_id2)


            c = 0
            while True:
                test = await b.call(method, params, raw=True)
                deal_list = test['result']
                for i in deal_list:
                    c += 1
                    deal_id = i['ID']
                    params['start'] += 1  # Увеличиваем начальную позицию для следующего запроса

                if len(deal_list) < 50:
                    count_abon += c
                    if category_id == 23:
                        region = 'Чуй'
                        await testik(region,c)
                        break  # Если меньше 50 сделок, значит, это последняя порция данных
                    elif category_id == 29:
                        region = 'Исык-кол'
                        await testik(region,c)
                        break  # Если меньше 50 сделок, значит, это последняя порция данных
                    elif category_id == 30:
                        region = 'Талас'
                        await testik(region,c)
                        break  # Если меньше 50 сделок, значит, это последняя порция данных
                    elif category_id == 31:
                        region = 'Нарын'
                        await testik(region,c)
                        break  # Если меньше 50 сделок, значит, это последняя порция данных
                    elif category_id == 32:
                        region = 'Ош'
                        await testik(region,c)
                        break  # Если меньше 50 сделок, значит, это последняя порция данных
                    elif category_id == 33:
                        region = 'Джалал-абад'
                        await testik(region,c)
                        break  # Если меньше 50 сделок, значит, это последняя порция данных
                    
        await count_podkl(count_abon)
        return c

while True:
    asyncio.run(podkl())
    time.sleep(90)

