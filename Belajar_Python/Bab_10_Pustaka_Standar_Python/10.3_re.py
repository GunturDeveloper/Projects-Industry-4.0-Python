import re

# Mencocokkan pola dengan regular expressions
pattern = r'\d+'
text = 'Ada 123 angka di sini'

matches = re.findall(pattern, text)
print("Angka yang ditemukan:", matches)
