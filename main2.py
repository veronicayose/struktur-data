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
    
class DataStruct:
    def __init__(self):
        self.items = None
        self.antrian = None
