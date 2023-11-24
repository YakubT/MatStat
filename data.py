import requests
import datetime
import json
import random

date = datetime.date(2020,3,19)
number = []
for i in range(1000):
    number.append(i)
random.shuffle(number)
f = open("data.txt", "w")
for i in range(100):
    date2 = date+datetime.timedelta(days=number[i])
    s = str(date2).split('-')
    s = s[0]+s[1]+s[2]
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date="+s+"&json"
    obj = requests.get(url).json()
    curses = obj
    eur = 1
    usd = 1
    for i in range(len(curses)):
        if (curses[i]["cc"]=="USD"):
            usd = curses[i]["rate"]
        if (curses[i]["cc"]=="EUR"):
            eur = curses[i]["rate"]
    f.write(str(eur/usd)+"\n")
    
print("end")
f.close()

