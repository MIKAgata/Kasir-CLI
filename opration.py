import os

def get_help():
    with open("help.txt", "r") as file:
        isi = file.read()
        print(isi)


def clear():
    os.system("cls" if os.name == "nt" else "clear")

