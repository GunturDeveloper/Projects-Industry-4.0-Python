# Fungsi rekursif untuk menghitung faktorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Faktorial dari 5:", factorial(5))
