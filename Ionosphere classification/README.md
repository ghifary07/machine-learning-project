# Klasifikasi data ionosphere

## 📌 Deskripsi  
Proyek ini bertujuan untuk melakukan klasifikasi data struktur elektron pada lapisan ionosphere menggunakan neural network Single layer Perceptron(SLP).  

## Tools yang Digunakan  
- Python (Pandas, Seaborn, Matplotlib, Scikit-Learn, Numpy, tensorflow, ann_visualizer)  
- Jupyter Notebook  

## Dataset  
Dataset ini berisi data pengembalian deteksi radar pada lapisan ionosphere bumi. Data radar ini dikumpulkan oleh sebuah sistem di Goose Bay, Labrador. Sistem ini terdiri dari susunan bertahap 16 antena frekuensi tinggi dengan total daya yang dipancarkan sekitar 6,4 kilowatt. Label atau target dari data ini adalah elektron bebas di Ionosfer yaitu "Good" dan "Bad".
+ Good menunjukan bahwa terdapat suatu struktur elektron di lapisan Ionosfer
+ Bad menunjukan bahwa tidak ada struktur elektron di Ionosfer.

Dataset didapat dari UCI dengan link: [Ionosphere dataset](https://archive.ics.uci.edu/dataset/52/ionosphere).  

## Steps
**1. Exploratory data analysis(EDA)** - mengetahui deskripsi dataset, distribusi data pada tiap label serta korelasi tiap fitur. Dataset ini memiliki total data sebanyak 351 yang berisi nilai-nilai pengembalian radar. Setiap pengembalian akan menghasilkan 17 pasang (34 buah) bilangan kompleks. Semua nilai pada attribut ini bersifat kontinu dan tidak memiliki missing value di dalamnya. Pada label Good akan mengembalikan nilai 1 dan Bad akan mengembalikan nilai 0.

**2. . Preprocessing** -  dalam preprocessing dilakukan pereduksian jumlah fitur menggunakan Principal Component Analysis(PCA). Selain itu dilakukan oversampling untuk menyeimbangkan distribusi data pada tiap label. Terakhir adalah pembagian data menjadi data training dengan rasio 57% data training dan 43% data testing.

**3. Klasifikasi dengan SLP** -  Model ditraining menggunakan neural network single layer perceptron(SLP) dengan menggunakan berbagai parameter yang berbeda. Parameter yang dibandingkan adalah jumlah neuron, seed, fungsi aktivasi, optimizer, dan learning rate awal.

## Hasil  
Model **SLP** terbaik didapat menggunakan parameter jumlah neuron=34, fungsi aktivasi=tanh, optimizer=adam, dan learning rate awal=0,1 memberikan akurasi dengan nilai **0.94**.