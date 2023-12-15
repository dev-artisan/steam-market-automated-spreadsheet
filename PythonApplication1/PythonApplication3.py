from traceback import print_last
import steammarket as sm
import json as js
import time

txt = open("prices.txt","w")
txt_items = open("items.txt","r")
items = []

for i in txt_items:
    i = i.rstrip("\n")
    items.append(i)


p = int(len(items)/20)
N = 0
P = 1

txt.close()

txt = open("prices.txt","a")

for x in items:
    if (int(N/P == 20)) & (P <= p):
            time.sleep(60)
            P = P + 1

    item = sm.get_csgo_item(x)
    z = js.dumps(item)
    y = js.loads(z)

    print(x + ":" + y["median_price"] + "\n")
    txt.write(x + ":" + y["median_price"] + "\n")
    
    N = N + 1
    
print("done")

txt.close()
