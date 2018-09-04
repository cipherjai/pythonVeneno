import json

with open("revw.json", encoding = 'utf-8-sig') as json_file:
    text = json_file.read()
    json_data = json.loads(text)
    print(json_data)

json_data
