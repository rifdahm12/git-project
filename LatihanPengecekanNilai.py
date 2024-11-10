# Rifdah Mahirah
# 2402870
# RPL 1A

print("Cek predikat nilai matkul daspro")
nilai = int(input("Masukkan nilai: "))
if (nilai >= 90):
    print(f"Nilai Anda adalah {nilai}, Anda mendapat predikat A")
elif (nilai < 90 and nilai >= 80):
    print(f"Nilai Anda adalah {nilai}, Anda mendapat predikat B")
elif (nilai < 80 and nilai >= 70):
    print(f"Nilai Anda adalah {nilai}, Anda mendapat predikat C")
elif (nilai < 70):
    print(f"Nilai Anda adalah {nilai}, Anda mendapat predikat D")