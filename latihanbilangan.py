# Rifdah Mahirah
# 2402870
# RPL 1A

angka = int(input("Masukkan angka: "))
if (angka >= 0):
    print(f"{angka} adalah bilangan positif")
    if (angka % 2 == 0):
        print(f"{angka} adalah bilangan genap")
    else:
        print(f"{angka} bilangan ganjil")
elif (angka < 0):
    print(f"{angka} adalah bilangan negatif")
    if (angka % 2 == 0):
        print(f"{angka} adalah bilangan genap")
    else:
        print(f"{angka} adalah bilangan ganjil")