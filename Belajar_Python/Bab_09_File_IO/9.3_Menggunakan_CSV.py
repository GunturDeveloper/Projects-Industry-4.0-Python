import csv

# Menulis ke file CSV
with open("data.csv", "w", newline='') as csvfile:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'name': 'Guntur', 'age': 17})
    writer.writerow({'name': 'Ayu', 'age': 16})

# Membaca dari file CSV
with open("data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
