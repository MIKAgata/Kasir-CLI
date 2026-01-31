import mysql.connector
from tabulate import tabulate

def get_connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kasir"
    
    )
    return mydb



def get_tambahtable():
    db = get_connect()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produk (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nama VARCHAR(100),
            harga INT,
            stok INT
        )
    """)
    db.commit()
    db.close()
 

def tambah_produk(nama, harga, stok):
    db = get_connect()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM produk WHERE nama = %s", (nama,))
    if cursor.fetchone():
        print(f"Produk '{nama}' sudah ada!")
    else:
        cursor.execute(
            "INSERT INTO produk (nama, harga, stok) VALUES (%s, %s, %s)",
            (nama, harga, stok)
        )
        db.commit()
        print(f"Produk '{nama}' berhasil ditambahkan!")

    db.close()


def hapus_produk(nama):
    db = get_connect()         
    cursor = db.cursor()       
    cursor.execute("SELECT * FROM produk WHERE nama = %s", (nama,))

    if cursor.fetchone() is None:
        print(f"Produk '{nama}' tidak ditemukan!")
    else:
        cursor.execute("DELETE FROM produk WHERE nama = %s", (nama,))
        db.commit()            # nyimpan perubahan
        print(f"Produk '{nama}' berhasil dihapus!")
        cursor.execute("TRUNCATE TABLE produk")


    db.close()                 



def get_produk():
    db = get_connect()
    cursor = db.cursor()

    cursor.execute("SELECT id, nama, harga, stok FROM produk")
    produk = cursor.fetchall()

    if not produk:
        print("Data produk masih kosong")
        return

    header = ["ID", "Nama Produk", "Harga", "Stok"]
    print(tabulate(produk, headers=header, tablefmt="grid"))

    db.close()




mydb = get_connect()


# get_tambahtable()

mydb.commit()

print("Koneksi berhasil dan tabel siap")





