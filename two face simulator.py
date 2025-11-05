# Game tebak koin
import random

koin = random.choice(["angka", "gambar"])
tebak = input("Tebak koin (angka/gambar): ")

if tebak not in ["angka", "gambar"]:
    print("Jawaban tidak valid. Harus 'angka' atau 'gambar'.")
elif tebak == koin:
    print("Benar! Anda Selamat!")
else:
    print("Salah! Innalillahi!", koin)
