import get_database as rm
import opration as op
from colorama import Fore, Style, init


def get_admin():
    rm.get_connect()
    # print("""
    #     Pilih opsi:\n
    #         1. Tambah produk
    #         2. Restok produk
    #         3. Tampilkan produk (-P)   #bingung mau isi apa
    #         4. 
            


    # """)

    while True:
        cmd = input(Fore.LIGHTRED_EX + "(admin)/"+Fore.WHITE + "kasir> ")
        if cmd == "restok" or cmd == "admin -k":
            pass

        elif cmd == "clear":
            op.clear()

        elif cmd == "kasir -h" or cmd == "kasir --help":
            op.get_help()

        elif cmd == "kasir -P":
            rm.get_produk()
        else:
            pass