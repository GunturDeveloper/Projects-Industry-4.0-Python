import json

# Menulis ke file JSON
data = {
    "name": "Guntur",
    "age": 17
}

with open("data.json", "w") as jsonfile:
    json.dump(data, jsonfile, indent=4)

# Membaca dari file JSON
with open("data.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print("Data JSON:", data)
