## 📌 Deskripsi  
Proyek ini bertujuan untuk melakukan analisis trend genre video games berdasarkan jumlah salinan game yang terjual pada tahun 2006 - 2016 . Selain itu juga dilakukan analisis penjualan beberapa publisher dan membuat model prediksi menggunakan neural network.  

## Tools yang Digunakan  
- Python (Pandas, Matplotlib, Sqlite)  
- Google colab

## Dataset  
Dataset ini berisi data penjualan video game di berbagai platform, genre, dan wilayah. Dataset ini berisi 16.600 baris data dan terdiri dari 11 atribut. Atribut penjualan dibagi menjadi penjualan pada wilayah Jepang, Eropa, Amerika utara, dan wilayah lain. 

Dataset didapat dari kaggle dengan link: [Video Games Sales](https://www.kaggle.com/datasets/anandshaw2001/video-game-sales/data).  

## Steps
**1. Import dan cleaning dataset** -  dataset diimport nmenggunakan pandas lalu dilakukan pembersihan data dengan menghilangkan data duplikat dan data yang missing. Setelah proses pembersihan data, jumlah data yang tersisa sebanyak 16.540 baris data. Data yang sudah dibersihkan kemudian diekspor ke dalam file excel "output.xlsx" untuk dianalisa menggunakan pivot table.

**2. Analisa data** -  Data yang telah diekspor kemudian diolah dengan # 📌 Deskripsi  
Proyek ini bertujuan untuk melakukan analisis trend genre video games berdasarkan jumlah salinan game yang terjual pada tahun 2006 - 2016 . Selain itu juga dilakukan analisis penjualan beberapa publisher dan membuat model prediksi menggunakan neural network.  

## Tools yang Digunakan  
- Python (Pandas, Matplotlib, Sqlite)  
- Google colab

## Dataset  
Dataset ini berisi data penjualan video game di berbagai platform, genre, dan wilayah. Dataset ini berisi 16.600 baris data dan terdiri dari 11 atribut. Atribut penjualan dibagi menjadi penjualan pada wilayah Jepang, Eropa, Amerika utara, dan wilayah lain. 

Dataset didapat dari kaggle dengan link: [Video Games Sales](https://www.kaggle.com/datasets/anandshaw2001/video-game-sales/data).  

## Steps
**1. Import dan cleaning dataset** -  dataset diimport nmenggunakan pandas lalu dilakukan pembersihan data dengan menghilangkan data duplikat dan data yang missing. Setelah proses pembersihan data, jumlah data yang tersisa sebanyak 16.540 baris data. Data yang sudah dibersihkan kemudian diekspor ke dalam file excel "output.xlsx" untuk dianalisa menggunakan pivot table.

**2. Analisa data** -  Data yang telah diekspor kemudian diolah dengan menggunakan pivot table sehingga dihasilkan 4 tabel hasil. Tabel tersebut terdiri dari tabel dengan 10 publisher, game, dan platform dengan total penjualan tertinggi dantabel data penjualan per wilayah serta global dari seluruh genre game.
* Tabel 10 publisher dengan total penjualan terbanyak
![publisher](/images/1.png)
* Tabel 10 games dengan total penjualan terbanyak 
![games](/images/2.png)
* Tabel penjualan pada seluruh genre game
![genre](/images/3.png)
* Tabel 10 platform dengan total penjualan terbanyak  
![platform](/images/4.png)

**3. Visualisasi data** - Visualisasi data tiap tabel hasil analisa dibuat menjadi sebuah dashboard pada microsoft excel menggunakan pivot chart dan slicer.
* Grafik penjualan dari 10 publisher dengan penjualan game terbanyak
![publisher](/images/51.png)
* Grafik penjualan 10 games dengan penjualan terbanyak dari setiap wilayah
![games](/images/52.png)
* Grafik penjualan seluruh genre game pada setiap wilayah
![genre](/images/53.png)
* Grafik penjualan dari 10 platform dengan penjualan terbanyak
![platform](/images/54.png)
* Tampilan penuh dashboard
![dashboard](/images/5.png)

**4. Pembuatan model** - Data penjualan yang telah dibersihkan juga digunakan untuk melatih model neural network untuk memprediksi banyaknya game yang terjual secara global. Model nerural network yang digunakan merupakan multi layer perceptorn regressor dengan jumlah neuron sebanyak 30 pada hidden layer dan fungsi aktivasi relu. Optimizer yang digunakan adalah Adaptive Moment Estimation(Adam). Model dilatih sebanyak 200 iterasi. Data yang digunakan dibagi menjadi data latih dan data uji dengan rasio 80:20. 
![model](/images/6.png)
Hasilnya didapat nilai rmse sebesar 0,0191 dari hasil pengujian model menggunakan data uji
![hasil](/images/7.png)

## Kesimpulan  
Dari hasil analisa data sebelumnya dapat diambil kesimpulan sebagai berikut:  
**1.** Penjualan game dari sebagian besar publisher rata-rata mengalami penurunan dari tahun 2015 sampai 2016. Hal ini sangat terbukti pada publisher nintendo yang mengalami penurunan drastis dari tahun 2006.
**2.** Sebagian besar games dengan penjualan terbanyak dipublish oleh nintendo dengan wii sports menjadi game dengan jumlah penjualan terbesar sebanyak 82,74 juta salinan. Lalu disusul dengan GTA V dengan jumlah penjualan sebanyak 55,92 juta salinan. Namun game GTA V memiliki jumlah penjualan yang sangat sedikit pada wilayah jepang.   
**3.** Game bergenre action memiliki penjualan yang besar pada wilayah eropa dan amerika utara. Sedangkan untuk wilayah jepang game dengan genre role playing lebih disukai karena memiliki jumlah penjualan yang lebih besar dibandingkan dengan genre lainnya.   
**4.** Game dengan genre puzzle dan strategi memiliki jumlah penjualan yang paling sedikit pada periode ini.  
**5.** Platform dengan penjualan game terbanyak adalah Xbox360 dengan penjualan sebesar 20% dari total seluruh penjualan game. Kemudian disusul dengan wii dan ps3 yang memiliki penjualan masing-masing sebesar 19% dari total seluruh penjualan game.