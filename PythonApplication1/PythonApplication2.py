from traceback import print_last
import steammarket as sm
import json as js
import time

txt_items = open("items.txt","r")
items = []
for i in txt_items:
    i = i.rstrip("\n")
    items.append(i)
txt_items.close()


cas = time.localtime()
akt_cas = cas.tm_yday
#txt_prices = open("prices.txt","r")
s_day = open("prices_7d.txt","r")
get_sday = int(s_day.readline())
m_day = open("prices_30d.txt","r")
get_mday = int(m_day.readline())

if akt_cas >= get_mday + 30:
    m_day = open("prices_30d.txt","w")
    txt_prices = open("prices_7d.txt","r")
    for i in txt_prices:
        i = i.rstrip("\n")
        m_day.write( i + "\n")
    txt_prices.close()
    m_day.close()
elif akt_cas >= get_sday + 7:
    s_day = open("prices_7d.txt","w")
    s_day.write(str(akt_cas) + "\n")
    txt_prices = open("prices.txt","r")
    for i in txt_prices:
        i = i.rstrip("\n")
        s_day.write( i + "\n")
    txt_prices.close()
    s_day.close()


p = int(len(items)/20)
N = 0
P = 1

txt_prices = open("prices.txt","w")   
txt_prices.close()


txt_prices = open("prices.txt","a")

for x in items:
    if (int(N/P == 20)) & (P <= p):
            time.sleep(60)
            P = P + 1

    item = sm.get_csgo_item(x)
    z = js.dumps(item)
    y = js.loads(z)

    print(x + ":" + y["median_price"] + "\n")
    txt_prices.write(x + ":" + y["median_price"] + "\n")
    
    N = N + 1
    
print("done")




txt_prices.close()
