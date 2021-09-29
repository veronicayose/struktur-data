import os
import math
# Jose Ryu Leonesta
class Barang:
    def __init__(self, namaBarang: str, kodeBarang: str, stokBarang: int):
        self.namaBarang = namaBarang
        self.kodeBarang = kodeBarang
        self.stokBarang = stokBarang


def binarySearch(arr, valueToSearch, x=0, y=-1, key=lambda x: x.kodeBarang):
    if (y == -1):
        y = len(arr)

    middleIndex = int(x + (y - x) / 2)

    if (y <= x):
        return -1
    
    if (key(arr[middleIndex]) == valueToSearch):
        return middleIndex
    
    if (key(arr[middleIndex]) < valueToSearch):
        return binarySearch(arr, valueToSearch, middleIndex + 1, y, key)
    
    if (key(arr[middleIndex]) > valueToSearch):
        return binarySearch(arr, valueToSearch, x, middleIndex, key)

def sort(arr, key=lambda x, y: x.kodeBarang > y.kodeBarang):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if key(arr[i], arr[j]):
                arr[i], arr[j] = arr[j], arr[i]

def fetchData(arr, lowerBound, upperBound):
    result = []

    if upperBound >= len(arr):
        upperBound = len(arr)

    for i in range(lowerBound, upperBound):
        result.append(arr[i])
    
    return result

def filter(arr, searchKey):
    result = []
    for x in arr:
        if searchKey.lower() in x.namaBarang.lower() or searchKey.lower() in x.kodeBarang.lower():
            result.append(x)
    
    return result

def showDataWithPagination(arr, rowsPerPage=5, currentPage=1, searchKey=""):
    lowerBound = rowsPerPage * currentPage - rowsPerPage
    upperBound = rowsPerPage * currentPage
 
    print(f"Halaman: {currentPage} dari {math.ceil(len(arr) / rowsPerPage)}")
    print(f"Jumlah barang: {len(arr)}")
    if len(searchKey):
        print(f"Kata cari: '{searchKey}'")

    fetchedData = fetchData(arr, lowerBound, upperBound)

    viewData(fetchedData, lowerBound + 1)
    print("Pilihan: ")
    print("1. Halaman selanjutnya")
    print("2. Halaman sebelumnya")
    print("3. Ganti jumlah baris per halaman")
    print("4. Cari barang")
    print("5. Keluar")
    userInput = inputInt("Pilih menu: ", 5, 1)

    if userInput == 1:
        os.system("cls")
        if upperBound >= len(arr):
            showDataWithPagination(arr, rowsPerPage, currentPage, searchKey)
        else:
            showDataWithPagination(arr, rowsPerPage, currentPage + 1, searchKey)

    if userInput == 2:
        os.system("cls")
        if lowerBound <= 0:
            showDataWithPagination(arr, rowsPerPage, currentPage, searchKey)
        else:
            showDataWithPagination(arr, rowsPerPage, currentPage - 1, searchKey)
    
    if userInput == 3:
        rowsPerPage = inputInt("Masukan jumlah baris perhalaman: ", lowerBound = 1)
        os.system("cls")
        showDataWithPagination(arr, rowsPerPage, searchKey=searchKey)
    
    if userInput == 4:
        searchKey = input("Masukan kata cari: ")
        newArr = filter(arr, searchKey)
        os.system("cls")
        if len(newArr) == 0:
            print(f"Tidak menemukan barang dengan kata kunci '{searchKey}'")
            showDataWithPagination(arr, rowsPerPage)
        else:
            showDataWithPagination(newArr, rowsPerPage, searchKey=searchKey)
# END Jose


#Veronica Yose Ardilla
def updateData(arr):
    ulang = 'y'
    while ulang == "Y" or ulang =='y':
        cariKode = str(input("Kode Barang : "))
        hasilCari = binarySearch(arr, cariKode)
        if hasilCari == -1:
            print("\nKode Barang tidak ditemukan")
        else:
            pilihan = inputInt("----SILAHKAN PILIH----\n1. Ubah Nama Barang\n2. Ubah Stok Barang\nPilih Menu : ", 2, 1)
            if pilihan == 1:
                arr[hasilCari].namaBarang = ''
                while arr[hasilCari].namaBarang == '':
                    arr[hasilCari].namaBarang = str(input("Masukkan nama barang baru : "))
                    if arr[hasilCari].namaBarang == '':
                        print("Nama Barang tidak boleh kosong")
            else :
                arr[hasilCari].stokBarang = inputInt("Masukkan stok barang baru : ", lowerBound=0)
        ulang = input("Ulangi? (Y/n): ")


def viewData(arr, startingNo=1):
    print("\n----------DAFTAR---------")
    print('{:>1} {:>2} {:>1} {:>20} {:>1} {:>14} {:>1} {:>14} {:>1}' .format("|", "No", "|", "Nama Barang", "|", "Stok Barang", "|", "Kode Barang", "|"))
    for x in range (len(arr)):
        no = startingNo + x
        line_new = '{:>1} {:>2} {:>1} {:>20} {:>1} {:>14} {:>1} {:>14} {:>1}' .format("|", no, "|", arr[x].namaBarang, "|", arr[x].stokBarang, "|", arr[x].kodeBarang, "|")
        print(line_new)

# END Veronica

# Melania
def deleteData(arr):
    ulang = 'y'
    while ulang == "Y" or ulang =='y':
        kodeBarang = input("Masukan Kode Barang : ")
        posisiBarang = binarySearch(arr, kodeBarang)
        if posisiBarang == -1:
                print("Barang tidak ditemukan")
        else:
            Konfirmasi = inputInt("Yakin ingin menghapus barang?\n1. Ya\n2. Tidak\nPilih Menu : ", 2, 1)
            if Konfirmasi == 1:
                del arr[posisiBarang]
                print('Barang{namaBarang} terhapus')
        
        ulang = input("Lanjut menghapus barang (Y/n)? ")
# END Melania

# Rachel
def tambahBarang():
    kodebarang = input("Masukan Kode barang: ")
    Namabarang = input("Masukan Nama barang: ")
    Stok = input("Masukan Stok: ")
    list1 = [kodebarang,Namabarang,Stok]
    list2.append(list1)
    data = data + 1
# END Rachel

# Jose
def inputInt(prompt: str, upperBound: int = None, lowerBound: int = None):
    try:
        result = int(input(prompt))
        if (upperBound != None and lowerBound != None):
            if (result > upperBound or result < lowerBound):
                print(f"Masukan angka {lowerBound} s/d {upperBound}")
                return inputInt(prompt, upperBound, lowerBound)

            else:
                return result
        elif (upperBound != None):
            if (result > upperBound):
                print(f"Masukan angka kurang atau sama dengan {upperBound}")
                return inputInt(prompt, upperBound, lowerBound)
            else:
                return result

        elif (lowerBound != None):
            if (result < lowerBound):
                print(f"Masukan angka lebih atau sama dengan {lowerBound}")
                return inputInt(prompt, upperBound, lowerBound)
            else:
                return result
        
        else:
            return result

    except ValueError:
        print("Hanya boleh memasukan angka")
        return inputInt(prompt, upperBound, lowerBound)

def main():
    print("Selamat datang di program CRUD Barang")
    print("Pilih menu:")
    print("1. Lihat daftar barang")
    print("2. Tambah barang")
    print("3. Ubah barang")
    print("4. Hapus barang")
    print("5. Mengurutkan barang")
    print("6. Keluar")
    pilihan = inputInt("Pilih menu: ", 6, 1)
    if pilihan == 1:
        os.system("cls")
        showDataWithPagination(arr)
        os.system("cls")
    elif pilihan == 2:
        tambahBarang()
    elif pilihan == 3:
        updateData(arr)
    elif pilihan == 4:
        deleteData(arr)
    elif pilihan == 5:
        sort(arr)
        print("Data telah diurutkan berdasarkan kode")
        input("Tekan enter untuk melanjutkan...")
        os.system("cls")
    elif pilihan == 6:
        print("Terimakasih...")
        exit()
    
    main()

ulangi = "y"
arr = [Barang('Testing', '1', 1), Barang('Test', '2', 1), Barang('Ing', 'Test', 1), Barang('Ingatan', '4', 1)]

while ulangi == "y" or ulangi == "Y":
    os.system("cls")
    main()
    ulangi = input("Ulangi main menu (Y/n)? ")