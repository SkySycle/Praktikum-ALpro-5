def cek_angka(a, b, c):
    if a != b and b != c and a != c:
        if a + b == c or a + c == b or b + c == a:
            return True
    return False

# Contoh TestCase
#print(cek_angka(3, 5, 8))  # True (karena 3 + 5 = 8)
#print(cek_angka(4, 6, 10)) # True (karena 4 + 6 = 10)
#print(cek_angka(2, 2, 4))  # False (karena ada angka yang sama)
#print(cek_angka(1, 2, 3))  # True (karena 1 + 2 = 3)
#print(cek_angka(5, 10, 15)) # True (karena 5 + 10 = 15)
#print(cek_angka(3, 3, 6))   # False (karena ada angka yang sama)
#print(cek_angka(1, 4, 6))   # False (tidak ada dua angka yang jika dijumlahkan sama dengan yang lain)