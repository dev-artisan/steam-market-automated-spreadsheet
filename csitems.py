import sys
import time
import steammarket
from datetime import datetime

def write_to_file(items, filename="prices.csv"):
    date = datetime.now()
    print(date.isoformat())

    with open(filename, "w") as file:
        for item in items:
            # Sleep it to avoid rate limiting and returning nothing
            time.sleep(2)

            result = steammarket.get_csgo_item(item, currency=currency)
            output = f"{date.isoformat()},{item},{result.get('median_price') if result else 'Not Found'}\n"
            
            print(output)
            file.write(output)


def main(filename, currency):
    items = []
        
    with open(filename, "r") as txt_items:
        for line in txt_items:
            line = line.strip("\n")
            items.append(line)
    
    write_to_file(items)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a filename")
        exit()
    
    currency = "EUR"
    if len(sys.argv) > 2:
        currency = sys.argv[2]
    
    main(filename=sys.argv[1], currency=currency)
    print("Bingo")