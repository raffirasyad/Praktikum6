from tabulate import tabulate

dataMahasiswa = {
    'No' : [],
    'Nim': [],
    'Nama': [],
    'Tugas' : [],
    'Uts' : [],
    'Uas' : [],
    'Nilai akhir' : [],
}
no = 0

def tampilkan():
    print("Berikut data yang tersedia ")
    print(tabulate(dataMahasiswa, headers=[ 
        'No', 'Nim','Nama', 'Tugas', 'Uts', 'Uas', 'Nilai Akhir'], tablefmt="fancy_grid"))

def tambah(no):
    nama = input("Masukan Nama :  ")
    nim = int(input("Masukan NIM :  ")) 
    tugas= int(input("Masukan Nilai Tugas :  "))
    uts = int(input("Masukan Nilai Uts :  "))
    uas  = int(input("Masukan Nilai Uas :  "))
    nilai_akhir = (tugas * 30 / 100 ) + (uts * 35 / 100) + (uas * 35 / 100)

    dataMahasiswa['No'].append(no)
    dataMahasiswa['Nim'].append(nim)
    dataMahasiswa['Nama'].append(nama)
    dataMahasiswa['Uts'].append(uts)
    dataMahasiswa['Tugas'].append(tugas)
    dataMahasiswa['Uas'].append(uas)
    dataMahasiswa['Nilai akhir'].append(nilai_akhir)
    print('Data berhasil ditambahkan. ')

def ubah(nama):
        if nama in dataMahasiswa['Nama']:

            namaIndex = dataMahasiswa['Nama'].index(nama)
            print("Pilih Data yang akan dirubah")

            while True:
                editApa = int(input(
                "(1) Nim, \n (2) Nama, \n (3) Nilai Tugas, \n (4) Nilai Uts, \n (5) Nilai Uas, \n (0) Simpan Perubahan & keluar \n :"))
                print("")

                if editApa == 1:
                    newNim = int(input("Masukan Nim : "))
                    dataMahasiswa['Nim'][namaIndex]=newNim
                elif editApa == 2:
                    newNama = input("Masukan Nama : ")
                    dataMahasiswa['Nama'][namaIndex] = newNama
                elif editApa == 3:
                    newTugas = int(input("Masukan Nilai Tugas : "))
                    nilai_akhir = (newTugas * 30 / 100) + (dataMahasiswa['Uts'][namaIndex] * 35 / 100) + (
                        dataMahasiswa['Uas'][namaIndex] * 35 / 100 )
                    dataMahasiswa['Tugas'][namaIndex] = newTugas
                    dataMahasiswa['Nilai Akhir'][namaIndex]= nilai_akhir
                elif editApa == 4:
                    newUts = int(input("Masukan Nailai Uts : "))
                    nilai_akhir = (dataMahasiswa['Tugas'][namaIndex] * 30 / 100) + (newUts * 35 / 100) + (
                        dataMahasiswa['Uas'][namaIndex] * 35 / 100 )
                    dataMahasiswa['Uts'][namaIndex] = newUts
                    dataMahasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
                elif editApa == 5:
                    newUas = int(input("Masukan Nilai Uas : "))
                    nilai_akhir = (dataMahasiswa['Tugas'][namaIndex] * 30 / 100) + (dataMahasiswa['Uts'][namaIndex] * 35 / 100) + (
                    newUas * 35 / 100)
                    dataMahasiswa['Uas'][namaIndex] = newUas
                    dataMahasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
                elif editApa == 0:
                    print('Perubahan data berhasil disimpan')
                    break
            else :
                print("Data tidak berhasil ditemukan")

def hapus(nama):
    if nama in dataMahasiswa['Nama']:
        namaIndex = dataMahasiswa ['Nama'].index(nama)

        del dataMahasiswa['No'][namaIndex]
        del dataMahasiswa['Nim'][namaIndex]
        del dataMahasiswa['Nama'][namaIndex]
        del dataMahasiswa['Tugas'][namaIndex]
        del dataMahasiswa['Uts'][namaIndex]
        del dataMahasiswa['Uas'][namaIndex]
        del dataMahasiswa['Nilai akhir'][namaIndex]
        print("data berhasil dihapus. ")
    else:
        print("Data tidak ditemukan")

while True:
    tanya = input (
        "(C)Menambah data: \n(R)Melihat semua data : \n(U) Perbaruhi data : \n(D)Menghapus data : \n(Q)Keluar Program : ")
    if tanya == "C":
        while True:
            no += 1
            tambah  ( no )
            tambahdatalagi = input("Ingin menambahkan data ? (y/n) :")
            if tambahdatalagi == 'n' :
                    break
    elif tanya == 'R':
            tampilkan()
            print("")
    elif tanya == "U":
            print(tabulate(dataMahasiswa, headers= ['No', 'Nim', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tablefmt="fancy_grid"))
            nama = input('Masukan nama yang akan di rubah : ')
            print("")
            ubah(nama)
    elif tanya == "D":
            print(tabulate(dataMahasiswa, headers=['No', 'Nim', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tablefmt="fancy_grid"))
            nama = input('Masukan nama yang akan dihapus : ')
            print("")
            hapus(nama)
    elif tanya == "Q":
            print("")
            print("Anda telah keluar dari program .")
            break