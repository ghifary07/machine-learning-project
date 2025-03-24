# Retail store inventory analisis

## 📌 Deskripsi  
Proyek ini bertujuan untuk melakukan analisis inventory pada dataset inventory retail menggunakan sql dan pandas.  

## Tools yang Digunakan  
- Python (Pandas, Matplotlib, Sqlite)  
- Visual studio code

## Dataset  
Dataset ini merupakan dataset sintesis untuk menganalisis dan memperkirakan permintaan inventaris toko retail. Dataset ini berisi 73.100 baris data harian di berbagai toko dan produk dan terdiri dari 15 atribut termasuk atribut seperti penjualan, tingkat inventory, harga, cuaca, promosi, dan hari libur.

Dataset didapat dari kaggle dengan link: [Retail store inventory demand forecast](https://www.kaggle.com/datasets/anirudhchauhan/retail-store-inventory-forecasting-dataset).  

## Steps
**1. Pembuatan database** -  dataset dimasukkan kedalam database bengan nama tabel inventory. database disimpan secara lokal maenggunakan library sqlite3. Berikut adalah query pembuatan tabel inventory.
```python
# create table
create_table_query = '''CREATE TABLE IF NOT EXISTS inventory(
                date DATE NOT NULL,
                store_id VARCHAR(4) NOT NULL,
                product_id VARCHAR(5) NOT NULL,
                category VARCHAR(20) NOT NULL,
                region VARCHAR(5) NOT NULL,
                inventory_level INTEGER NOT NULL,
                units_sold INTEGER NOT NULL,
                units_ordered INTEGER NOT NULL,
                demand_forecast DECIMAL(5, 2) NOT NULL,
                price DECIMAL(5, 2) NOT NULL,
                discount INTEGER(3) NOT NULL,
                weather_condition VARCHAR(6) NOT NULL,
                holiday_promotion BOOLEAN NOT NULL,
                competitor_pricing DECIMAL(5, 2) NOT NULL,
                seasonality VARCHAR(6) NOT NULL);
                '''
```
Setelah itu data kemudian di import dari file csv ke tabel database.
```python
sqlite> .mode csv
sqlite> .import --csv --skip 1 retail_store_inventory.csv inventory
```

**2. EDA** -  Setelah itu dilakukan berbagai analisis pada data menggunakan query sql dan pandas berdasarkan kategori produk. Berikut adalah hasil analisis dataset:
* Total produk yang terjual per kategori
![sold](https://github.com/user-attachments/assets/9dddfd1e-21c2-4985-8111-0781dbf50a88)
* Total produk yang diorder per kategori
![order](https://github.com/user-attachments/assets/bff06e2c-c9d1-400e-bb5b-19fc5546352c)
* Perbandingan rata-rata harga produk per kategori dengan pesaing
![priceComp](https://github.com/user-attachments/assets/9b617e83-4ffe-4d1d-9377-0c39831537c6)
* Rata-rata prediksi permintaan produk per kategori pada toko 1
![S1demand](https://github.com/user-attachments/assets/d5a704db-885a-418a-b17d-9f3f9387a6c6)
* Rata-rata prediksi permintaan produk per kategori pada toko 2
![S2demand](https://github.com/user-attachments/assets/ae6077a7-5051-4ed6-848c-bc03d9921dee)
* Rata-rata prediksi permintaan produk per kategori pada toko 3
![S3demand](https://github.com/user-attachments/assets/cb578bff-70ce-498a-a054-8451f28d20cd)
* Rata-rata prediksi permintaan produk per kategori pada toko 4
![S4demand](https://github.com/user-attachments/assets/081a3760-ba4a-44ba-a883-87d5808c1c65)
* Rata-rata prediksi permintaan produk per kategori pada toko 5
![S5demand](https://github.com/user-attachments/assets/016e731f-e634-4f07-a140-0f7026546237)

**3. Visualisasi data** - Visualisasi data dilakukan untuk mempermudah membaca data dan mencari pola dari beberapa tabel hasil query. Berikut adalah hasil visualisasi data dari total penjualan, pemesanan barang ,dan penjualan tiap kategori barang per harinya.
* Total produk yang terjual per kategori
![sold](https://github.com/user-attachments/assets/ad008183-4bdb-4d1f-b036-cca4ac0ee83e)
* Total produk yang diorder per kategori
![order](https://github.com/user-attachments/assets/f65753f5-cf26-4f2d-a12f-dfb96a5f6f82)
* Total penjualan barang dengan kategori furniture per harinya
![furniture](https://github.com/user-attachments/assets/42762576-2a62-4120-bb2b-c8d401aea0f8)
* Total penjualan barang dengan kategori clothing per harinya
![clothing](https://github.com/user-attachments/assets/8e6e7fd6-c7a3-41a2-a838-7ded079071a2)
* Total penjualan barang dengan kategori toys per harinya
![toys](https://github.com/user-attachments/assets/f6810727-6d6b-4094-b41a-4564bce5897e)
* Total penjualan barang dengan kategori groceries per harinya
![groceries](https://github.com/user-attachments/assets/1e6bf6cb-2217-48f1-a649-88b34ffb293b)
* Total penjualan barang dengan kategori electronics per harinya
![electronics](https://github.com/user-attachments/assets/6d0fe888-a4e0-4ef2-97e1-66ae33ea8fef)

## Hasil  
Dari hasil query tabel dan hasil visualisasi data dapat diambil beberapa kesimpulan yaitu:  
**1.** Dari seluruh kategori produk, produk dengan kategori electronics dan toys memiliki total penjualan paling rendah. hal ini berpengaruh pada rata-rata harga barang pada kedua  kategori tersebut dimana harga barang lebih tinggi daripada harga yang dimiliki pesaing/competitor pada kategori yang sama.  
**2.** Untuk stok barang pada toko 1 berdasarkan rata-rata tingkat permintaan, barang yang diprioritaskan ketersediannya adalah barang dengan kategori groceries dan toys.   
**3.** Sedangkan untuk stok barang pada toko 2 berdasarkan rata-rata tingkat permintaan, barang yang diprioritaskan ketersediannya adalah barang dengan kategori groceries dan furniture.  
**4.** Untuk stok barang pada toko 3 berdasarkan rata-rata tingkat permintaan, barang yang diprioritaskan ketersediannya adalah barang dengan kategori toys dan furniture.  
**5.** Untuk stok barang pada toko 4 berdasarkan rata-rata tingkat permintaan, barang yang diprioritaskan ketersediannya adalah barang dengan kategori clothing dan groceries.  
**6.** Untuk stok barang pada toko 5 berdasarkan rata-rata tingkat permintaan, barang yang diprioritaskan ketersediannya adalah barang dengan kategori clothing dan furniture.  
**7.** Dari hasil visualisasi data penjualan barang per harinya dapat dilihat barang dengan kategori electronics dan clothing sedang mengalami penurunan penjualan. Oleh karena itu disarankan untuk mengadakan promo seperti diskon atau pembelian secara bundle untuk dapat bersaing dengan harga yang ditawarkan competitor.  

  