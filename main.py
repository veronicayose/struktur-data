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
            pilihan = int(input("\n----SILAHKAN PILIH----\n1. Ubah Nama Barang\n2. Ubah Stok Barang\nPilih Menu : "))
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
        ulang = input("\nUlangi? (Y/n): ")
        print("\n")

def viewData(arr):
    print("\n----------DAFTAR---------")
    print('{:>1} {:>2} {:>1} {:>20} {:>1} {:>14} {:>1} {:>14} {:>1}' .format("|", "No", "|", "Nama Barang", "|", "Stok Barang", "|", "Kode Barang", "|"))
    for x in range (len(arr)):
        no = x+1
        line_new = '{:>1} {:>2} {:>1} {:>20} {:>1} {:>14} {:>1} {:>14} {:>1}' .format("|", no, "|", arr[x].namaBarang, "|", arr[x].stokBarang, "|", arr[x].kodeBarang, "|")
        print(line_new)

# Melania
def deleteData(arr):
    namaBarang =  ["Barang ('B', '1', 1)", "Barang ('A', '2', 1)", "Barang ('C', '3', 1)", "Barang('D', '4', 1"]
    print(namaBarang)
    namaBarang.pop()
    print(namaBarang)

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
    pilihan = inputInt("Pilih menu: ", 5, 1)
    if pilihan == 1:
        viewData(arr)
    elif pilihan == 2:
        pass
    elif pilihan == 3:
        updateData(arr)
    elif pilihan == 4:
        deleteData(arr)
    elif pilihan == 5:
        sort(arr)

main()