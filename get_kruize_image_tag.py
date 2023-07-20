import json
import yaml

# Read YAML file
with open('kruize-clowdapp.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

# Write YAML object to JSON format
with open('/tmp/kruize-clowdapp.json', 'w') as f:
    json.dump(data, f, sort_keys=False)

# Read JSON file into Python dict
with open('/tmp/kruize-clowdapp.json', 'r') as f:
    json_data = json.load(f)

param = json_data["parameters"]
for data in param:
    if data["name"] == "KRUIZE_IMAGE_TAG":
        commit_tag=data["value"]
        print(data["value"])

with open('/tmp/.commitsha', 'w') as f:
    f.write(commit_tag)
    f.close()
