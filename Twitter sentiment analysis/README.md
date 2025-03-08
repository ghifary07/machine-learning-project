# Twitter sentimen analisis

## 📌 Deskripsi  
Proyek ini bertujuan untuk melakukan analisis sentimen terhadap tweet/opini masyarakat mengenai wabah cacar monyet dengan hashtag #WaspadaCacarMonyet.  

## Tools yang Digunakan  
- Python (Pandas, Sastrawi, tweepy, Scikit-Learn)  
- Jupyter Notebook  

## Dataset  
Dataset diambil dari twitter dengan crawling menggunakan library tweepy. Pelabelan dilakukan secara manual dengan tiga label sentimen yaitu positif, negatif, dan netral. Dataset dapat dilihat pada folder /Dataset. Dataset diambil pada tanggal **7 Juni 2022**.  

## Steps
**1. Crawling data tweet** - crawling dilakukan dengan menggunakan library tweepy dan API key yang disediakan twitter, sebanyak 1000 data tweet berhasil didapatkan. Data kemudian di filter untuk menhilangkan spam dan duplikat sehingga hasil akhirnya terdapat 854 data.

**2. Labelling** - pelabelan dilakukan dengan memberikan sentimen positif, negatif atau netral pada setiap tweet secata manual menggunakan google spreadsheet.

**3. Preprocessing** - preprocessing terdiri dari membersihkan teks untuk menghilangkan Seperti #(hashtag), simbol emote, dan hyperlink(http://), menghapus stopwords, dan stemming(mengubah tiap kata menjadi kata dasar). jumlah data setelah preprocessing adalah 774 data.

**4. Pembagian data** -  data kemudian dibagi menjadi 541 data training dan 233 data testing

**5. Vektorisasi** -  mengubah data teks menjadi angka atau vector yang nilainya merupakan angka kemunculan term atau kata unik pada data teks tersebut. Metode vektorisasi yang digunakan adalah Tf-Idf vectorizer.

**6. Pembuatan model** -  pelatihan dan uji model menggunakan algoritma Support Vector Machine(SVM).

## Hasil  
Model **SVM** memberikan akurasi terbaik dengan nilai **0.93**.
  