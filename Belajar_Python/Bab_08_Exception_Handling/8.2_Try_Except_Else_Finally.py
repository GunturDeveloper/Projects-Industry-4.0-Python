# Try, except, else, finally
try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File tidak ditemukan")
else:
    print("File dibaca dengan sukses")
finally:
    print("Operasi selesai")
