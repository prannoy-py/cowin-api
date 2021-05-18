import requests
import json
import time

headers = {"Accept-Language": "en_US", "Accept": "*/*",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51"
           }

param = {'pincode': '400056', 'date': '19-05-2021'}
# url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=400056&date=19-05-2021"
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"

while True:
    resp = requests.get(url=url,
                        params=param,
                        headers=headers)
    print(resp.url)
    print(resp.status_code)
    if resp.status_code == 200:
        data = resp.json()
        print(data)
        if data['centers'] != []:
            print('Check Now')
            break
        else:
            continue
    else:
        print(resp)
        time.sleep(0.8)
        continue
