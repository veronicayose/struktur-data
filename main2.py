import os
import math

class Barang:
    def __init__(self, namaBarang: str, kodeBarang: str, stokBarang: int):
        self.namaBarang = namaBarang
        self.kodeBarang = kodeBarang
        self.stokBarang = stokBarang

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
    # Jose
    def add(self, value, key=lambda x: x.kodeBarang):
        if key(value) == key(self.value):
            raise ValueError('Kode barang sudah digunakan')

        if key(value) < key(self.value):
            if self.left == None:
                self.left = BinaryTree(value)
            else:
                self.left.add(value)
        
        if key(value) > key(self.value):
            if self.right == None:
                self.right = BinaryTree(value)
            else:
                self.right.add(value)
    
    # Jose
    # Returns tuple(resultantList, currentIndex)
    def fetchData(self, amount: int, skip: int, result=None, currentIndex: int=0):
        if result == None:
            result = []
        if self.left != None:
            result, currentIndex = self.left.fetchData(amount, skip, result, currentIndex)

        if len(result) >= amount:
            return result, currentIndex
        
        if (currentIndex >= skip):
            result.append(Barang(
                self.value.namaBarang,
                self.value.kodeBarang,
                self.value.stokBarang
            ))

        currentIndex += 1

        if self.right != None:
            result, currentIndex = self.right.fetchData(amount, skip, result, currentIndex)

        return result, currentIndex

class DataStruct:
    def __init__(self):
        self.items = None
        self.antrian = None
        self.itemsCount = 0
    
    def add(self, value):
        if self.items == None:
            self.items = BinaryTree(value)
        else:
            self.items.add(value)
        self.itemsCount += 1

    # Jose
    def showDataWithPagination(self, rowsPerPage=5, currentPage=1):
        totalPage = math.ceil(self.itemsCount / rowsPerPage)
        print(f"Halaman: {currentPage} dari {totalPage}")
        print(f"Jumlah barang: {self.itemsCount}")
        print(f"Jumlah baris per halaman: {rowsPerPage}")

        fetchedData = self.items.fetchData(rowsPerPage, (currentPage - 1) * rowsPerPage)[0]
        showTable(self.items.fetchData(rowsPerPage, (currentPage - 1) * rowsPerPage)[0])
        print("Pilihan: ")
        print("1. Halaman selanjutnya")
        print("2. Halaman sebelumnya")
        print("3. Ganti jumlah baris per halaman")
        print("4. Cari barang")
        print("5. Keluar")
        userInput = inputInt("Pilih menu: ", 5, 1)

        if userInput == 1:
            os.system("cls")
            if currentPage < totalPage:
                self.showDataWithPagination(rowsPerPage, currentPage + 1)
            else:
                self.showDataWithPagination(rowsPerPage, currentPage)

        if userInput == 2:
            os.system("cls")
            if currentPage > 1:
                self.showDataWithPagination(rowsPerPage, currentPage - 1)
            else:
                self.showDataWithPagination(rowsPerPage, currentPage)

        if userInput == 3:
            rowsPerPage = inputInt("Masukan jumlha baris per halaman: ")
            os.system("cls")
            self.showDataWithPagination(rowsPerPage)
        
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

# Veronica
def showTable(arr, startingNo=1):
    print("\n----------DAFTAR---------")
    print('{:>1} {:>2} {:>1} {:>20} {:>1} {:>14} {:>1} {:>14} {:>1}' .format("|", "No", "|", "Nama Barang", "|", "Stok Barang", "|", "Kode Barang", "|"))
    for x in range (len(arr)):
        no = startingNo + x
        line_new = '{:>1} {:>2} {:>1} {:>20} {:>1} {:>14} {:>1} {:>14} {:>1}' .format("|", no, "|", arr[x].namaBarang, "|", arr[x].stokBarang, "|", arr[x].kodeBarang, "|")
        print(line_new)


struct = DataStruct()
struct.add(Barang('C', 'C', 2))
struct.add(Barang('B', 'B', 2))
struct.add(Barang('A', 'A', 2))
struct.add(Barang('T', 'T', 2))
struct.add(Barang('L', 'L', 2))

struct.showDataWithPagination(2)