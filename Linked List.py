class Node:
    def __init__(self, produk):
        self.produk = produk
        self.next = None

class DaftarProduk:
    def __init__(self):
        self.head = None

    def tambah_produk(self, produk):
        node_baru = Node(produk)
        if not self.head:
            self.head = node_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru

    def tampilkan_produk(self):
        current = self.head
        while current:
            print(current.produk, end=" -> ")
            current = current.next
        print("Selesai")

# Contoh penggunaan
produk_list = DaftarProduk()
produk_list.tambah_produk("Laptop")
produk_list.tambah_produk("Smartphone")
produk_list.tampilkan_produk() 
