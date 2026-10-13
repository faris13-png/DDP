kendaraan = ["avanza","mobil","1500cc","hitam","4roda"]
print("list awal: ")
print(kendaraan)

# menambahkan harga dan tipe kendaraan di belakang
kendaraan.append("243 juta")
kendaraan.append("CVT")

# menambahkan merek kendaraan
kendaraan.insert(2,"toyota")

print("\nlist kendaraan setelah ditambahkan :")
print(kendaraan)

# soal ke 2
print("silahkan pilih bangun datar")
print("1. persegi")
print("2. lingkaran")
print("3. segitiga")

pilih_bangun_datar = int(input("pilih bangun datar: "))

match pilih_bangun_datar:

    case 1:
        sisi = float(input("masukkan sisi:"))
        luas = sisi * sisi
        print("luas persegi =", luas)

    case 2:
        jari = float(input("masukkanjari jari:"))
        luas = 3.14 * jari ** 2
        print("luas lingkaran=", luas)

    case 3:
        alas = float(input("masukkan alas:"))
        tinggi = float(input("masukkan tinggi:"))
        luas = 0.5 * alas * tinggi
        print("luas segitiga=", luas)

    case _:
         print("kamu salah pilih")
