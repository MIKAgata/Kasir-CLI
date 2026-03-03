<<<<<<< HEAD
#CLI KASIR
=======
# Masih dalam tahap pengembangan
>>>>>>> 4e2ef04acdd6b6e8a709ffe9a581bc7f7fbfe1d8

aplikasi kasil 
masih tahap awal berupa CLI
aplikasi akan berjalan dengan skema barang dinput dan terakhir ditotalkan, lalu dikurangkan dengan diskon jika ada.
lalu dijumlahkan kembali dengan uang pelanggan.
lalu terdapat fitur untuk menambahkan produk atau mengurangi, megedit diskon 


##FITUR
query join tabel

SELECT 
    t.id_transaksi,
    t.tanggal,
    p.nama_produk,
    d.qty,
    p.harga,
    d.subtotal
FROM detail_transaksi d
JOIN transaksi t ON d.id_transaksi = t.id_transaksi
JOIN produk p ON d.id_produk = p.id;

guery paling laku
SELECT 
    p.nama_produk,
    SUM(d.qty) AS total_terjual
FROM detail_transaksi d
JOIN produk p ON d.id_produk = p.id
GROUP BY d.id_produk
ORDER BY total_terjual DESC;


