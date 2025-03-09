c_to_f = lambda c: (9/5) * c + 32
c_to_r = lambda c: 0.8 * c

print("Hasil konversi:")
print("100°C ->", c_to_f(100), "F")
print("80°C  ->", c_to_r(80), "R")
print("0°C   ->", c_to_f(0), "F")

#Contoh TestCase
#print(celcius_to_fahrenheit(100))  # 212 (karena 100°C = 212°F)
#print(celcius_to_reamur(80))       # 64 (karena 80°C = 64°R)
#print(celcius_to_fahrenheit(0))    # 32 (karena 0°C = 32°F)