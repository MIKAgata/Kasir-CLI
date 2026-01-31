import get_database as rm
import opration as op
import admin as ad
from colorama import Fore, Style, init


init(autoreset=True)



op.clear()

print(Fore.CYAN + Style.BRIGHT + r"""
██╗  ██╗  █████╗   ███████╗ ██╗ ██████╗ 
██║ ██╔╝ ██╔══██╗  ██╔════╝ ██║ ██╔══██╗
█████╔╝  ███████║  ███████╗ ██║ ██████╔╝
██╔═██╗  ██╔══██║  ╚════██║ ██║ ██╔══██╗
██║  ██╗ ██║  ██║  ███████║ ██║ ██║  ██║    
╚═╝  ╚═╝ ╚═╝  ╚═╝  ╚══════╝ ╚═╝ ╚═╝  ╚═╝
    
""")

print(Fore.YELLOW + "Selamat datang di aplikasi kasir,\n ketik kasir -h untuk melihat opsi \n ketik exit jika mau keluar\n")



while True:
    cmd = input(Fore.GREEN + "kasir> ")
    rm.get_connect()

    if cmd == "exit":
        print(Fore.RED + "Thanks")
        break

    elif cmd == "clear":
        op.clear()

    elif cmd == "kasir -h" or cmd == "kasir --help":
        op.get_help()

    elif cmd == "kasir -P":
        rm.get_produk()

    elif cmd == "kasir -g admin":
        ad.get_admin()

    else:
        print(cmd)




















