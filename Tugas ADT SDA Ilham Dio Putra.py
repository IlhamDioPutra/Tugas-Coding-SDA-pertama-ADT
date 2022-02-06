#Tugas coding adt ilham dio putra NPM G1A021024 dalam membuat ADT code terstruktur
#membuat code menghitung luas dan keliling persegi panjang
class Menghitung_volume_dan_Luas_persegiPanjang :
    #fungsi class pada python ini adalah membuat berbagai banyak
    #bagian bagian fungsi yang ada sehingga bisa memanggl ulang kode-
    #kode yang terlah kita buat
    
    panjang = int
    lebar = int
    #kedua code diatas adalah untuk mengklarifikasikan dulu variabel
    #yang telah kita buat termasuk apa

    panjang = int(input("panjang persegi :"))
    lebar = int(input("lebar persegi :"))
    #kedua code diatas ditunjukkan agar kita bisa memasukkan nilai
    #variabel yang kita inginkan

    luas_persegi_panjang = panjang * lebar
    keliling_persegi_panjang = 2 * ( panjang + lebar )
    #code diatas adalah variabel rumus untuk menghitung
    #keliling dan luas persegi panjang kita

    print("Jadi luas persegi panjangnya adalah : ",luas_persegi_panjang,)
    print("Jadi keliling persegi panjangnya adalah : ",keliling_persegi_panjang,)
    #ini adalah print akhir untuk menghitung luas dan keliling persegi panjang yang  ingin kita buat
    



