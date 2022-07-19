import json
import os

toolMaterial = ['wooden', 'stone', 'iron', 'golden', 'diamond', 'netherite']
toolType = ['shovel', 'axe', 'pickaxe', 'sword', 'hoe']
item = ['paper']
itemName = '이름'

file_list = os.listdir(f'{os.path.dirname(__file__)}') # file name load
file_list.remove(os.path.basename(__file__)) # same name remove
file_list.remove('.DS_Store') # mac default folder remove
print(file_list) 

with open(f'{os.path.dirname(__file__)}/resorcepack/paper.json', 'r') as f:
    json_data = json.load(f)
# print(json.dumps(json_data, indent="\t"))

model_number = json_data['overrides'][0]['predicate']['custom_model_data'] #custom model data load
model_name = json_data['overrides'][0]['model'] #item file name load

row = {
    "predicate": {
        "custom_model_data": 100000000
    },
    "model": "item/" + itemName
}

# print(json_data)

json_data['overrides'][0].update(row)


with open('krVerFile.json', 'w') as outfile:
    json.dump(json_data, outfile, ensure_ascii=False, indent="\t")
