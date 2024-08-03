import os

# Membuat direktori
os.makedirs("new_directory", exist_ok=True)

# Menghapus direktori
os.rmdir("new_directory")

# Mengecek keberadaan file atau direktori
print("Apakah file ada:", os.path.isfile("sample.txt"))
print("Apakah direktori ada:", os.path.isdir("new_directory"))
