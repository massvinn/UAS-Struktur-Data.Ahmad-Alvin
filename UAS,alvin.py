import csv
import os

FILE_NAME = "Ahmad Alvin Raditya.csv"

# ==========================
# NODE LINKED LIST
# ==========================

class Node:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = float(ipk)
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, nim, nama, jurusan, ipk):
        new_node = Node(nim, nama, jurusan, ipk)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        print("\nDATA MAHASISWA")
        print("-"*60)

        while current:
            print(
                f"NIM: {current.nim} | "
                f"Nama: {current.nama} | "
                f"Jurusan: {current.jurusan} | "
                f"IPK: {current.ipk}"
            )
            current = current.next

    def search(self, nim):
        current = self.head

        while current:
            if current.nim == nim:
                return current
            current = current.next

        return None

    def delete(self, nim):
        current = self.head
        prev = None

        while current:
            if current.nim == nim:

                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next

                return current

            prev = current
            current = current.next

        return None

    def to_list(self):
        data = []

        current = self.head

        while current:
            data.append([
                current.nim,
                current.nama,
                current.jurusan,
                current.ipk
            ])

            current = current.next

        return data


# ==========================
# STACK
# ==========================

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None


undo_stack = Stack()

# ==========================
# CSV
# ==========================

def load_data():
    ll = LinkedList()

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                ll.append(
                    row["nim"],
                    row["nama"],
                    row["jurusan"],
                    row["ipk"]
                )

    return ll


def save_data(ll):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "nim",
            "nama",
            "jurusan",
            "ipk"
        ])

        current = ll.head

        while current:
            writer.writerow([
                current.nim,
                current.nama,
                current.jurusan,
                current.ipk
            ])

            current = current.next


# ==========================
# SORTING
# ==========================

def sort_nama(ll):
    data = ll.to_list()

    n = len(data)

    for i in range(n):
        for j in range(n-i-1):

            if data[j][1].lower() > data[j+1][1].lower():
                data[j], data[j+1] = data[j+1], data[j]

    print("\nDATA TERURUT NAMA")

    for d in data:
        print(d)


def sort_ipk(ll):
    data = ll.to_list()

    n = len(data)

    for i in range(n):
        for j in range(n-i-1):

            if float(data[j][3]) < float(data[j+1][3]):
                data[j], data[j+1] = data[j+1], data[j]

    print("\nDATA TERURUT IPK")

    for d in data:
        print(d)


# ==========================
# MENU
# ==========================

def menu():

    ll = load_data()

    while True:

        print("\n===== MENU =====")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Cari Data")
        print("6. Sort Nama")
        print("7. Sort IPK")
        print("8. Undo Delete")
        print("9. Keluar")

        pilih = input("Pilih Menu: ")

        if pilih == "1":

            nim = input("NIM: ")
            nama = input("Nama: ")
            jurusan = input("Jurusan: ")
            ipk = input("IPK: ")

            ll.append(nim, nama, jurusan, ipk)

            save_data(ll)

            print("Data berhasil ditambahkan.")

        elif pilih == "2":

            ll.display()

        elif pilih == "3":

            nim = input("Masukkan NIM: ")

            data = ll.search(nim)

            if data:
                data.nama = input("Nama Baru: ")
                data.jurusan = input("Jurusan Baru: ")
                data.ipk = float(input("IPK Baru: "))

                save_data(ll)

                print("Data berhasil diupdate.")

            else:
                print("Data tidak ditemukan.")

        elif pilih == "4":

            nim = input("Masukkan NIM: ")

            deleted = ll.delete(nim)

            if deleted:
                undo_stack.push(deleted)

                save_data(ll)

                print("Data berhasil dihapus.")

            else:
                print("Data tidak ditemukan.")

        elif pilih == "5":

            nim = input("Masukkan NIM: ")

            hasil = ll.search(nim)

            if hasil:
                print(
                    hasil.nim,
                    hasil.nama,
                    hasil.jurusan,
                    hasil.ipk
                )
            else:
                print("Data tidak ditemukan.")

        elif pilih == "6":
            sort_nama(ll)

        elif pilih == "7":
            sort_ipk(ll)

        elif pilih == "8":

            data = undo_stack.pop()

            if data:
                ll.append(
                    data.nim,
                    data.nama,
                    data.jurusan,
                    data.ipk
                )

                save_data(ll)

                print("Undo berhasil.")
            else:
                print("Tidak ada data.")

        elif pilih == "9":
            break

        else:
            print("Menu tidak valid.")


menu()