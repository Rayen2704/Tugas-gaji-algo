#Variabel

print(" ██▀███  ▓██   ██▓ ▄▄▄       ███▄    █  ")
print("▓██ ▒ ██▒ ▒██  ██▒▒████▄     ██ ▀█   █  ")
print("▓██ ░▄█ ▒  ▒██ ██░▒██  ▀█▄  ▓██  ▀█ ██▒ ")
print("▒██▀▀█▄    ░ ▐██▓░░██▄▄▄▄██ ▓██▒  ▐▌██▒ ")
print("░██▓ ▒██▒  ░ ██▒▓░ ▓█   ▓██▒▒██░   ▓██░ ")
print("░ ▒▓ ░▒▓░   ██▒▒▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒  ")
print("  ░▒ ░ ▒░ ▓██ ░▒░   ▒   ▒▒ ░░ ░░   ░ ▒░ ")
print("  ░░   ░  ▒ ▒ ░░    ░   ▒      ░   ░ ░  ")
print("   ░      ░ ░           ░  ░         ░  ")
print("          ░ ░                           ")

nama = str(input("Masukkan Nama Karyawan  : "))
JamMasuk        = int(input("Jam masuk kerja         : "))
print("SELAMAT PAGI",nama)
print()

JamKeluar       = int(input("Jam keluar kerja        : "))
print("SELAMAT",nama)
print()
print() 

#rumus
Jammasukkerja           = JamKeluar - JamMasuk
gajipokok          = 175000

jamnormal = 8
if (Jammasukkerja > 8):
    lembur = Jammasukkerja - jamnormal
    Lembur1 = lembur * 15000
else:
    Lembur1 = 0

totalgaji = gajipokok + Lembur1

print("-----RINCIAN GAJI-----")
print("NAMA              :",nama)
print("WAKTU KERJA       :",Jammasukkerja)
print("GAJI PERHARI      :",gajipokok)
print("LEMBUR            :",Lembur1,'(',JamMasuk,'sd',JamKeluar,')')
print("TotalGaji         :",totalgaji)    