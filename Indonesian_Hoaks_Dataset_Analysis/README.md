## 📌 Deskripsi  
Di era misinformasi yang merajalela, akses ke data terverifikasi dan dapat dibaca mesin dari sumber resmi sangat penting bagi para peneliti, ilmuwan data, dan pengembang yang ingin membangun perangkat dan model untuk memerangi penyebarannya. Proyek ini bertujuan untuk mengidentifikasi entitas-entitas penting pada data berita hoaks indonesia dari tahun 2018 - 2025 menggunakan library spacy. Proyek ini bertujuan untuk mengetahui entitas-entitas yang sering ditemui pada berita hoaks serta frekuensi kemunculannya pada waktu tertentu. 

## Tools yang Digunakan  
- Python (Pandas, spacy, matplotlib)  
- Google colab

## Dataset  
Dataset ini mencakup klarifikasi berita hoaks yang bersumber langsung dari web resmi pemerintah Indonesia untuk klarifikasi hoaks melalui portal Direktorat Komunikasi Digital, komdigi.go.id. Dataset ini memiliki 16563 baris data dan 13 fitur, termasuk topik berita dan jumlah pembaca untuk setiap berita.

Dataset didapat dari kaggle dengan link: [Indonesian Hoaks news](https://www.kaggle.com/datasets/ireddragonicy/indonesian-hoax-news-dataset).  

## Steps
**1. Import dataset dan model NLP** -  dataset diimport nmenggunakan pandas, sedangkan model NLP yang digunakan adalah id_core_news_sm yang dibuat oleh firqaaa. Link sumber model : [Indonesian NLP model by firqaaa](https://huggingface.co/firqaaa/id_core_news_sm)

**2. Analisa data** -  Data yang telah diimpor kemudian dianalisa untuk mengetahui distribusi beserta jumlah total pembaca tiap topik pada data dan trend topik tiap tahunnya.
* Grafik distribusi topik dan total pembacanya
![topicview](/Indonesian_Hoaks_Dataset_Analysis/Pictures/TopicView.PNG)
* Grafik trend frekuensi tiap topik hoaks
![topictrend](/Indonesian_Hoaks_Dataset_Analysis/Pictures/TopicTrend.PNG)
Terlihat dari grafik diatas, topic hoaks memiliki jumlah dan frekuensi kemunculan yang besar dibandingkan dengan topik lainnya. Jumlah berita hoaks meningkat besar pada akhir tahun 2019 dan awal 2020. Jumlah berita hoaks semakin menurun setelah periode tersebut.

**3. Named Entity Recognition (NER)** - Menggunakan model spacy yang telah diimport, dilakukan proses NER menggunakan library spacy. Dari proses tersebut didapatkan 18 label entitas deangan entitas yang paling banyak disebut merupakan entitas dengan label PERSON, GPE(Geo Political Entity), dan ORG(Organization). Dari proses NER didapat 15 entitas yang paling sring muncul dalam teks berita. namun, masih terdapat beberapa kata yang salah terdeteksi sebagai entitas atupun kesalahan pada labelnya.
* Grafik distribusi label nama entitas
![entitydis](/Indonesian_Hoaks_Dataset_Analysis/Pictures/NERTrend.PNG)
* 15 entitas yang paling banyak muncul
![common](/Indonesian_Hoaks_Dataset_Analysis/Pictures/1.PNG)

**4. Perbaikan dan pembersihan label data entitas** - Data entitas yang telah didapat kemudian dibersihkan dan diperbaiki untuk mendapatkan hasil yang lebih akurat. Pembersihan dilakukan dengan menghapus kata-kata yang bukan termasuk entitas seperti "dilansir" dan "link counter". Sedangkan perbaikan data dilakukan dengan menambahkan pattern atau label yang benar pada entitas dengan kesalahan label. Contohnya Jakarta dideteksi sebagai ORG(Organization) diubah menjadi GPE(Geo Political Entity) dan Covid dari PERSON menjadi EVENT.  
![wronge](/Indonesian_Hoaks_Dataset_Analysis/Pictures/WrongE.PNG)
Hasilnya didapat nilai rmse sebesar 0,0191 dari hasil pengujian model menggunakan data uji
![rule](/Indonesian_Hoaks_Dataset_Analysis/Pictures/EditE.PNG)
Setelah dilakukan pembersihan didapat 15 entitas yang paling sering muncul dalam teks berita yang lebih akurat.
![commontrue](/Indonesian_Hoaks_Dataset_Analysis/Pictures/common.PNG)

## Kesimpulan  
Dari hasil analisa data sebelumnya dapat diambil kesimpulan sebagai berikut:  
**1.** Frekuensi kemunculan berita hoaks meningkat pada akhir tahun 2019 dan awal tahun 2020, waktu ini bertepatan dengan terjadinya penyebaran virus covid-19 di seluruh dunia. Hal ini juga sesuai dengan hasil NER yang menunjukkan Covid menjadi salah satu entitas yang paling sering muncul di berita hoaks yaitu sebanyak 4240 kali.
**2.** Tahun 2019 dan 2024 merupakan entitas tahun yang paling sering muncul pada teks berita. Tahun 2019 merupkan awal terjadinya bencana COVID. Sedangkan pada tahun 2024 diselenggarakan pemilihan umum untuk memilih presiden negara republik indonesia. Joko Widodo, presiden Indonesia sebelumnya menjadi entitas PERSON yang paling sering muncul. Hal ini menunjukkan banyaknya berita hoaks yang menyebut nama Jokowi pada masa menjelang pemilu 2024.    