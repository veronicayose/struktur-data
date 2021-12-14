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
