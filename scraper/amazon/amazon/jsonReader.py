import json

# with open("revw.json", encoding = 'utf-8-sig') as json_file:
#     text = json_file.read()
#     json_data = json.loads(text)
#     print(json_data)


# checking latest f commit
# Note that dump() takes two positional arguments: (1) the data object to be serialized, and (2) the file-like object to which the bytes will be written.

# [list {dictionary -> (xyz : list[ ], )}]

# Product name, details, most recent 100 reviews with review details
with open("revw.json", encoding="utf-8-sig") as json_file:
    text = json_file.read()
    data = json.loads(text)
    print(list(data))
