import get_database as rm
import opration as op
from colorama import Fore


def get_admin():

    # rm.get_tambahtable()  # pastikan tabel ada

    while True:
        cmd = input(Fore.LIGHTRED_EX + "(admin)/" + Fore.WHITE + "kasir> ").strip().lower()

        if cmd == "clear":
            op.clear()

        elif cmd in ["kasir -h", "kasir --help"]:
            op.get_help()

        elif cmd == "kasir -p":
            rm.get_produk()

        elif cmd == "kasir -t":
            try:
                nama = input("Nama produk: ")
                harga = int(input("Harga produk: "))
                stok = int(input("Stok produk: "))

                rm.tambah_produk(nama, harga, stok)
                rm.get_produk()

            except ValueError:
                print("Harga dan stok harus berupa angka")

        elif cmd in ["exit", "quit"]:
            print("Keluar dari admin mode")
            break

        else:
            print("Command tidak dikenal. Ketik 'kasir -h'")