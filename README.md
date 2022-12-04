# Praktikum6
Latihan 1 
Ubah kode di bawah ini menjadi fungsi menggunakan lambda

``` pyhton
import math

def a(x):
return x**2

def b(x, y):
return math.sqrt(x**2 + y**2)

def c(*args):
return sum(args)/len(args)

def d(s):
return "".join(set(s))
Ubahlah kode dibawah ini menjadi fungsi menggunakan lambda.

```

1. Membuat folder dan file baru pada viscode

<img width="131" alt="foto 1" src="https://user-images.githubusercontent.com/115473988/205491948-e182ed3e-ff7f-4f26-86e6-f35e5956f85d.png">

2. masukan kodingan berikut
``` pyhton
import math

def a(n): return lambda x: x**n

lambdaA = a (4)
print(lambdaA(4))

def b(i,j):
    return lambda x, y : math.sqrt(x**i + y**j )

lambdaB = b(4, 0)
print(lambdaB(3, 0))

def c(*args):
    return lambda *params :sum(args) / len(params)

lambdaC = c(1,2,3,4,5)
print(lambdaC(2,2,5))

def d(firstname):
    return lambda * lastname: "".join(set(firstname)) + "".join(set(lastname))

lambdaD = d("M")
print(lambdaD("Raffi", "Rasyad"))
````

3. Hasil setelah di run

<img width="401" alt="foto 2" src="https://user-images.githubusercontent.com/115473988/205491991-c9cb1bcd-8235-403c-8447-d7b786bc4294.png">

# Tugas Praktikum

Buat program sederhana dengan mengaplikasikan penggunaan fungsi
yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan:
Fungsi tambah() untuk menambah data
Fungsi tapilkan() untuk menampilkan data
Fungsi hapus(nama) untuk menghapus data berdasarkan nama
Fungsi ubah(nama) untuk mengubah data berdasarkan nama
Buat flowchart dan penjelasan programnya pada README.md. • Commit dan push repository ke github.

1. Membuat flowchart
![foto 3](https://user-images.githubusercontent.com/115473988/205492085-d2de6c06-ac37-4eb4-b8d6-df712e2bbdc9.png)

2. Masukan kodingan berikut

``` pyhton

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
```

3. jalankan program edit / hapus data sesuka kita, dengan memasukan perintah perintah yang tertera seperti contoh berikut :

<img width="766" alt="foto 4" src="https://user-images.githubusercontent.com/115473988/205492248-6311c90a-5c4f-4e8c-b673-85ea811db71d.png">

<img width="596" alt="foto 5 1" src="https://user-images.githubusercontent.com/115473988/205492254-8f5320b7-3bbf-4a14-922c-8eacca42c125.png">

<img width="623" alt="foto 5" src="https://user-images.githubusercontent.com/115473988/205492256-45f7f844-0e8d-4cd2-a276-d215da5d99c3.png">

<img width="625" alt="foto 6" src="https://user-images.githubusercontent.com/115473988/205492259-f442047a-1d58-4ca5-9513-43ec379cc375.png">

M. Raffi Rasyad

TI.22.B1

