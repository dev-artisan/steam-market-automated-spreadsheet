# Counter-Strike Steam market price reader

This python program fetches your desired items and puts them in a .csv file for you to use in a spreadsheet and keep track on your cs2 items

To set up run:
```bash
pip install -r requirements.txt
```

Prepare a text file with your items (using the item name as it is in the steam market) on separate lines.
e.g. `weapons.txt` or `cases.txt`

Run the below:
```bash
python csitems.py weapons.txt USD
```

This will produce two files:
 - A History file `weapons.history.json`
 - A data csv file `weapons.output.csv`

The csv file has the following columns:
 - Date
 - Item
 - Price

You can open the file in Excel and use a pivot table to track averages or graph the data.
