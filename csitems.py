import sys
import time
import json
import steammarket
from datetime import datetime


def get_items(filename):
    items = []
    with open(filename, "r") as txt_items:
        for line in txt_items:
            line = line.strip("\n")
            if line:
                items.append(line)
    return items


def get_history(name):
    try:
        with open(f"{name}.history.json", "r") as file:
            history = json.loads(file.read())
    except FileNotFoundError as e:
        history = {}

    return history


def clean_up_history(history, items):
    """This function removes all items from history that are not longer in the items file"""
    new_history = {}
    for date, date_data in history.items():
        new_data = {}
        for item, item_data in date_data.items():
            if item in items:
                new_data[item] = item_data
        if new_data:
            new_history[date] = new_data
    return new_history


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
    items = get_items(filename)

    history = get_history(name)
    history = clean_up_history(history, items)

    date = datetime.now().date()
    isodate = date.isoformat()
    print(isodate)

    for item in items:
        # Sleep it to avoid rate limiting and returning nothing
        time.sleep(3)

        result = steammarket.get_csgo_item(item, currency=currency)
        data = history.get(isodate, {})
        if result and result.get("success") is True:
            print(result)

            data[item] = result
        else:
            print("Cannot retrieve item: ", item, result)
            data[item] = {"success": False, "median_price": "N/A"}
        history[isodate] = data

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
    print("######  Bingo  ######")
