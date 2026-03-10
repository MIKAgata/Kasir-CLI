import get_database as rm
import opration as op
import admin as ad
from colorama import Fore, Style, init

init(autoreset=True)


def banner():
    op.clear()
    print(Fore.CYAN + Style.BRIGHT + r"""
██╗  ██╗  █████╗   ███████╗ ██╗ ██████╗ 
██║ ██╔╝ ██╔══██╗  ██╔════╝ ██║ ██╔══██╗
█████╔╝  ███████║  ███████╗ ██║ ██████╔╝
██╔═██╗  ██╔══██║  ╚════██║ ██║ ██╔══██╗
██║  ██╗ ██║  ██║  ███████║ ██║ ██║  ██║    
╚═╝  ╚═╝ ╚═╝  ╚═╝  ╚══════╝ ╚═╝ ╚═╝  ╚═╝
""")

    print(
        Fore.YELLOW
        + "Selamat datang di aplikasi kasir\n"
        + "ketik 'kasir -h' untuk melihat opsi\n"
        + "ketik 'exit' untuk keluar\n"
    )


def get_kasir():

    while True:
        cmd = input(Fore.GREEN + "kasir> ").strip().lower()

        if cmd == "exit":
            print(Fore.RED + "Terima kasih telah menggunakan kasir")
            break

        elif cmd == "clear":
            op.clear()

        elif cmd in ["kasir -h", "kasir --help"]:
            op.get_help()

        elif cmd == "kasir -p":
            rm.get_produk()

        elif cmd == "kasir -g admin":
            ad.get_admin()

        elif cmd == "transaksi":
            print("Fitur transaksi belum dibuat")

        else:
            print(Fore.RED + "Command tidak dikenali. Ketik 'kasir -h'")




banner()
get_kasir()