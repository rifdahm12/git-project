# Rifdah Mahirah
# 2402870
# RPL 1A

print("Selamat datang para calon model. Silahkan masukkan data diri Anda.")

nama = str(input("Masukkan nama lengkap Anda: "))
jenis_kelamin = str(input("Masukkan jenis kelamin Anda (Wanita/Pria): "))
umur = int(input("Masukkan umur Anda: "))
tinggi_badan = int(input("Masukkan tinggi badan Anda: "))
iq = int(input("Berapa skor IQ Anda: "))

if (umur >= 18 and umur <= 25):
    pass
    if (jenis_kelamin == "Wanita" and tinggi_badan >= 170):
        pass
        if (iq >= 130):
            pass
            if (True):
                print(f"Selamat {nama}! Kamu lolos seleksi menjadi model.")
        else:
            print("Maaf Anda tidak lolos seleksi menjadi model.")
    elif (jenis_kelamin == "Pria" and tinggi_badan >= 175):
        pass
        if (iq >= 130):
            pass
            if (True):
                print(f"Selamat {nama}! Kamu lolos seleksi menjadi model.")
        else:
            print("Maaf Anda tidak lolos seleksi menjadi model.")
    else:
        print("Maaf Anda tidak lolos seleksi menjadi model.")
else:
    print("Maaf Anda tidak lolos seleksi menjadi model.")