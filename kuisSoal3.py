# Rifdah Mahirah
# 2402870
# RPL 1A

panjang = float(1000) #centimeter
lebar = float(8) #meter
tinggi = float(350) #centimeter
panjang_ke_meter = float(panjang/100)
tinggi_ke_meter = float(tinggi/100)
luas_permukaan = float(2*(panjang_ke_meter*tinggi_ke_meter) + 2*(lebar*tinggi_ke_meter))
total_biaya = float(luas_permukaan*580000)
print(f"Total biaya yang dibutuhkan adalah Rp{total_biaya}")