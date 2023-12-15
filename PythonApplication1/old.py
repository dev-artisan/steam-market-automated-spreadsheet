import steammarket as sm
import json as js
import time

txt = open("prices.txt","w")

# 20 items an array
items = ["Stockholm 2021 Champions Autograph Capsule", "Antwerp 2022 Contenders Autograph Capsule", "Antwerp 2022 Champions Autograph Capsule", "Antwerp 2022 Challengers Sticker Capsule", "Antwerp 2022 Contenders Sticker Capsule", "Antwerp 2022 Challengers Autograph Capsule", "Antwerp 2022 Legends Sticker Capsule", "Antwerp 2022 Legends Autograph Capsule", "Rio 2022 Contenders Autograph Capsule", "Rio 2022 Champions Autograph Capsule", "Rio 2022 Challengers Sticker Capsule", "Rio 2022 Contenders Sticker Capsule", "Rio 2022 Challengers Autograph Capsule", "Rio 2022 Legends Sticker Capsule", "Rio 2022 Legends Autograph Capsule","Paris 2023 Contenders Autograph Capsule","Paris 2023 Champions Autograph Capsule","Paris 2023 Legends Autograph Capsule","Paris 2023 Challengers Autograph Capsule","Paris 2023 Challengers Sticker Capsule"]
items2 = ["Paris 2023 Contenders Sticker Capsule","Paris 2023 Legends Sticker Capsule","Sticker | jks (Holo) | Paris 2023","Sticker | m0NESY (Holo) | Paris 2023","Sticker | WOOD7 (Holo) | Paris 2023","Sticker | Natus Vincere (Holo) | Paris 2023","Sticker | FURIA (Holo) | Paris 2023","Operation Broken Fang Case","Operation Riptide Case","Sticker | Renegades (Holo) | Katowice 2019","Fracture Case","Snakebite Case"]
txt.close()

txt = open("prices.txt","a")

for x in items:
    item = sm.get_csgo_item(x)
    z = js.dumps(item)
    y = js.loads(z)
    print(x + ":" + y["lowest_price"])
    txt.write(x + ":" + y["lowest_price"] + "\n")

time.sleep(60)

for a in items2:
    item = sm.get_csgo_item(a)
    z = js.dumps(item)
    y = js.loads(z)
    print(a + ":" + y["lowest_price"])
    txt.write(a + ":" + y["lowest_price"] + "\n")

txt.close()
