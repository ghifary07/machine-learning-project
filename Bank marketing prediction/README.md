# Prediksi data marketing bank

## 📌 Deskripsi  
Proyek ini bertujuan untuk melakukan prediksi pada data marketing bank portugis dengan menggunakan neural network Multi Layer Perceptron(MLP).  

## Tools yang Digunakan  
- Python (Pandas, Seaborn, Matplotlib, Scikit-Learn, Numpy)  
- Jupyter Notebook  

## Dataset  
Dataset ini merupakan data kampanye marketing langsung dari sebuah lembaga perbankan Portugis. Kampanye pemasaran tersebut didasarkan pada panggilan telepon. Sering kali, diperlukan lebih dari satu kontak dengan klien yang sama, untuk mengetahui apakah produk (deposito berjangka bank) akan dibeli('yes') atau tidak dibeli('no'). File yang digunakan adalah bank-full.csv.

Dataset didapat dari UCI dengan link: [Bank marketing dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing).  

## Steps
**1. Preprocessing** -  dalam preprocessing dilakukan penghapusan data yang missing dan outlier data. Lalu dilakukan feature encoding, feature scaling, Principal Component Analysis(PCA) dan menghilangkan fitur yang tidak diperlukan untuk mempermudah model memprediksi data. Terakhir adalah pembagian data menjadi data training dengan rasio 80% data training dan 20% data testing.

**2. Klasifikasi dengan MLP** -  Model ditraining menggunakan neural network Multi layer perceptron(MLP) dengan menggunakan parameter 3 hidden layer dengan jumlah neuron (50, 200, 50), fungsi aktivasi=relu, dan optimizer=adam.

## Hasil  
Model **MLP** mendapatkan akurasi sebesar **0.85** dan nilai Mean Squared Error(MSE) sebesar **0.153**.
  