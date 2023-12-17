import sys
import time
import json
import steammarket
from datetime import datetime

def get_history(name):
    try:
        with open(f"{name}.history.json", "r") as file:
            history = json.loads(file.read())
    except FileNotFoundError as e:
        history = {}

    return history

def write_history(name, history):
    print("Writing History")
    print(json.dumps(history))
    with open(f"{name}.history.json", "w") as file:
        file.write(json.dumps(history))
    
    
def write_output_csv(name, history):
    print("Writing CSV")
    with open(f"{name}.output.csv", "w") as file:
        file.write("Date,Item,Price")
        for date, date_data in history.items():
            for item, item_data in date_data.items():
                output = f"{date},{item},{item_data.get('median_price')}\n"
                file.write(output)
    
    
def main(filename, currency):
    name = filename.split(".")[0]
    history = get_history(name)
    items = []
        
    with open(filename, "r") as txt_items:
        for line in txt_items:
            line = line.strip("\n")
            items.append(line)
    
    date = datetime.now().date()
    isodate = date.isoformat()
    print(isodate)

    for item in items:
        # Sleep it to avoid rate limiting and returning nothing
        time.sleep(3)

        result = steammarket.get_csgo_item(item, currency=currency)
        if result and result.get("success") is True:
            print(result)

            data = history.get(isodate, {})
            data[item] = result
            history[isodate] = data
        else:
            print("Cannot retrieve item: ", item, result)
        
        
    write_history(name, history)
    write_output_csv(name, history)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a filename")
        exit()
    
    currency = "EUR"
    if len(sys.argv) > 2:
        currency = sys.argv[2]
    
    main(filename=sys.argv[1], currency=currency)
    print("Bingo")