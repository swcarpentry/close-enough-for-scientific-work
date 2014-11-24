import json

with open("settings.json", 'r') as f:
    settings = json.loads(f.read())


print settings["spring_constant"]
