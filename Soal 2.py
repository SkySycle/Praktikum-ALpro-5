def cek_digit_belakang(a, b, c):
    last_a = a % 10
    last_b = b % 10
    last_c = c % 10
    return (last_a == last_b) or (last_a == last_c) or (last_b == last_c)

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

print(cek_digit_belakang(a, b, c))

#Contoh TestCase
#print(cek_digit_belakang(30, 20, 18))    # True (karena 30 dan 20 memiliki digit belakang yang sama: 0)
#print(cek_digit_belakang(145, 5, 100))   # True (karena 145 dan 5 memiliki digit belakang yang sama: 5)
#print(cek_digit_belakang(71, 187, 18))   # False (karena tidak ada dua angka dengan digit belakang yang sama)
#print(cek_digit_belakang(1024, 14, 94))  # True (karena 14 dan 94 memiliki digit belakang yang sama: 4)
#print(cek_digit_belakang(53, 8900, 658)) # False (karena tidak ada dua angka dengan digit belakang yang sama)