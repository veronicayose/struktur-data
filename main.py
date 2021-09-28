# Jose Ryu Leonesta
class Barang:
    def __init__(self, namaBarang: str, kodeBarang: str, stokBarang: int):
        self.namaBarang = namaBarang
        self.kodeBarang = kodeBarang
        self.stokBarang = stokBarang

arr = [Barang('B', '1', 1), Barang('A', '2', 1), Barang('C', '3', 1), Barang('D', '4', 1)]

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

#Veronica Yose Ardilla
def updateData(arr):
    ulang = 'y'
    while ulang == "Y" or ulang =='y':
        cariKode = str(input("Kode Barang : "))
        hasilCari = binarySearch(arr, cariKode)
        if hasilCari == -1:
            print("\nKode Barang tidak ditemukan")
        else:
            pilihan = int(input("\n----SILAHKAN PILIH----\n1. Ubah Nama Barang\n2. Ubah Kode Barang\nPilih Menu : "))
            if pilihan == 1:
                arr[hasilCari].namaBarang = ''
                while arr[hasilCari].namaBarang == '':
                    arr[hasilCari].namaBarang = str(input("\nMasukkan nama barang baru : "))
                    if arr[hasilCari].namaBarang == '':
                        print("Nama barang tidak boleh kosong")
            elif pilihan == 2 :
                arr[hasilCari].stokBarang = ''
                while arr[hasilCari].stokBarang == '':
                    arr[hasilCari].stokBarang = int(input("\nMasukkan stok barang baru : "))
                    if arr[hasilCari].stokBarang == '':
                        print("Stok barang tidak boleh kosong")
            else:
                print("\nAngka tidak valid")
        ulang = input("\nUlangi? (y/n): ")
        print("\n")

def viewData(arr):
    print("\n----------DAFTAR---------")
    print('{:>1} {:>2} {:>1} {:>20} {:>1} {:>14} {:>1} {:>14} {:>1}' .format("|", "No", "|", "Nama Barang", "|", "Stok Barang", "|", "Kode Barang", "|"))
    for x in range (len(arr)):
        no = x+1
        line_new = '{:>1} {:>2} {:>1} {:>20} {:>1} {:>14} {:>1} {:>14} {:>1}' .format("|", no, "|", arr[x].namaBarang, "|", arr[x].stokBarang, "|", arr[x].kodeBarang, "|")
        print(line_new)

# Melania
namaBarang =  ["Barang ('B', '1', 1)", "Barang ('A', '2', 1)", "Barang ('C', '3', 1)", "Barang('D', '4', 1"]
print(namaBarang)
namaBarang.pop()
print(namaBarang)

# Jose
print("Selamat datang di program CRUD Barang")
print("Pilih menu:")
print("1. Lihat daftar barang")
print("2. Tambah barang")
print("3. Ubah barang")
print("1. Lihat daftar barang")