import json

def sort_json(package):
    return package['analytics']['365d']


with open('homebrew.json','r') as f:
    data = json.load(f)

# data = [item for item in data if 'A' in item['desc']]

# data.sort(key=sort_json,reverse=True)
data.sort(key=sort_json,reverse=True)

# data_str = json.dumps(data,indent=2)   ###we can use list slicing here if needed eg. data[:3]
# print(data_str)

with open ("sorted_json.json",'w') as f:
    json.dump(data,f,indent=2)

