# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Meskipun perusahaan ini telah berkembang menjadi entitas yang cukup besar, Jaya Jaya Maju masih menghadapi tantangan dalam mengelola karyawan mereka. 

Salah satu masalah utama yang dihadapi adalah tingginya tingkat attrition atau rasio jumlah karyawan yang keluar dibandingkan dengan total karyawan yang mencapai lebih dari 10%. Tingginya tingkat attrition ini menimbulkan berbagai masalah seperti meningkatnya biaya rekrutmen dan pelatihan, menurunnya produktivitas, serta dampak negatif pada moral karyawan yang tersisa.

Untuk mencegah masalah ini semakin parah, manajer departemen HR meminta bantuan untuk mengidentifikasi faktor-faktor yang mempengaruhi tingginya tingkat attrition tersebut. Selain itu, mereka juga membutuhkan sebuah business dashboard yang dapat membantu memonitor berbagai faktor tersebut secara real-time. Dengan adanya dashboard ini, manajemen HR dapat mengambil tindakan preventif dan strategis untuk mengurangi tingkat attrition dan meningkatkan retensi karyawan.

Proyek ini bertujuan untuk menganalisis data karyawan, mengidentifikasi faktor-faktor utama yang mempengaruhi attrition, dan membuat model prediksi yang dapat membantu perusahaan dalam mengambil keputusan yang lebih baik. Dashboard yang dihasilkan juga akan memberikan visualisasi yang jelas dan mudah dipahami mengenai berbagai metrik penting terkait karyawan dan attrition.

### Permasalahan Bisnis

Beberapa permasalahan bisnis utama yang akan diselesaikan dalam proyek ini adalah sebagai berikut:

1. **Tingginya Tingkat Attrition**:
   - Jaya Jaya Maju menghadapi masalah dengan tingkat attrition yang tinggi, mencapai lebih dari 10%. Tingginya tingkat attrition menyebabkan meningkatnya biaya rekrutmen dan pelatihan, serta menurunnya produktivitas dan moral karyawan yang tersisa.

2. **Identifikasi Faktor-faktor Penyebab Attrition**:
   - Manajer HR membutuhkan pemahaman yang mendalam mengenai faktor-faktor apa saja yang paling mempengaruhi keputusan karyawan untuk meninggalkan perusahaan. Tanpa pemahaman ini, akan sulit bagi manajemen untuk mengambil tindakan yang tepat untuk mengurangi tingkat attrition.

3. **Kekurangan Sistem Pemantauan**:
   - Saat ini, Jaya Jaya Maju tidak memiliki sistem yang efektif untuk memantau metrik-metrik penting terkait karyawan dan attrition. Manajemen membutuhkan business dashboard yang dapat menyediakan visualisasi data yang jelas dan real-time untuk membantu mereka dalam pengambilan keputusan.

4. **Pengambilan Keputusan yang Terinformasi**:
   - Dengan data dan informasi yang tersedia, manajemen HR perlu membuat keputusan yang terinformasi untuk meningkatkan retensi karyawan. Tanpa alat analitik yang tepat, keputusan yang diambil mungkin tidak berdasarkan data yang akurat dan relevan.

5. **Rekomendasi Tindakan**:
   - Selain mengidentifikasi faktor-faktor penyebab attrition, proyek ini juga harus memberikan rekomendasi tindakan yang dapat diimplementasikan oleh perusahaan untuk meningkatkan retensi karyawan dan mengurangi tingkat attrition.

Melalui analisis data karyawan dan pengembangan model prediksi, proyek ini bertujuan untuk memberikan wawasan yang dapat ditindaklanjuti mengenai faktor-faktor yang mempengaruhi attrition serta menyediakan alat berupa business dashboard untuk membantu manajemen HR dalam memantau dan mengelola karyawan secara lebih efektif.

### Cakupan Proyek

Cakupan proyek ini meliputi beberapa tahapan penting yang akan dikerjakan untuk mencapai tujuan yang telah ditetapkan. Berikut adalah cakupan proyek yang akan dilaksanakan:

1. **Pengumpulan Data**:
   - Mengumpulkan data karyawan yang mencakup informasi demografis, metrik terkait pekerjaan, dan status attrition dari file `employee_data.csv`.

2. **Analisis Data Awal**:
   - Melakukan eksplorasi dan analisis data awal untuk memahami distribusi dan karakteristik data karyawan.
   - Menangani data yang hilang dan membersihkan data untuk memastikan kualitas data yang digunakan dalam analisis lebih lanjut.

3. **Rekayasa Fitur**:
   - Menggunakan teknik rekayasa fitur untuk mengubah data mentah menjadi format yang lebih sesuai untuk analisis dan pemodelan.
   - Melakukan encoding pada fitur kategorikal menggunakan `LabelEncoder`.

4. **Pemodelan dan Prediksi**:
   - Melatih model machine learning untuk memprediksi attrition karyawan berdasarkan fitur-fitur yang ada.
   - Mengevaluasi performa model menggunakan metrik seperti precision, recall, dan accuracy.
   - Menyimpan model yang telah dilatih dan encoder yang digunakan.

5. **Pembuatan Dashboard Bisnis**:
   - Mengembangkan business dashboard menggunakan Tableau Public untuk memvisualisasikan metrik-metrik penting terkait karyawan dan attrition.
   - Dashboard akan mencakup visualisasi seperti scatter plot, bar chart, dan histogram yang membantu manajemen HR dalam memantau faktor-faktor yang mempengaruhi attrition.

6. **Prediksi Data Baru**:
   - Menyediakan skrip `prediction.py` yang dapat digunakan untuk memprediksi attrition pada data karyawan baru.
   - Skrip akan memuat model yang telah dilatih dan encoder yang digunakan untuk meng-encode data baru.

7. **Dokumentasi dan Laporan**:
   - Menyusun dokumentasi proyek yang mencakup semua tahapan yang telah dilakukan, hasil analisis, dan kesimpulan.
   - Menyusun README.md yang berisi deskripsi proyek, penggunaan, ikhtisar data, dan rekomendasi tindakan.

8. **Rekomendasi Tindakan**:
   - Berdasarkan hasil analisis dan model prediksi, memberikan rekomendasi tindakan yang dapat diambil oleh perusahaan untuk mengurangi tingkat attrition dan meningkatkan retensi karyawan.

Dengan cakupan proyek ini, diharapkan Jaya Jaya Maju dapat memiliki pemahaman yang lebih baik mengenai faktor-faktor yang mempengaruhi attrition karyawan dan dapat mengambil tindakan yang tepat untuk meningkatkan retensi karyawan.

### Persiapan

Sumber data: [employee_data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

Setup environment:

1. **Unduh Data**:
   - Unduh file `employee_data.csv` dari sumber data yang disediakan.

2. **Instalasi Pustaka yang Dibutuhkan**:
   - Pastikan Anda memiliki Python terinstal di sistem Anda.
   - Buat virtual environment untuk proyek ini (opsional tetapi disarankan).
     ```bash
     python -m venv env
     source env/bin/activate  # Untuk MacOS/Linux
     env\Scripts\activate  # Untuk Windows
     ```
   - Instal pustaka yang dibutuhkan menggunakan `requirements.txt`.
     ```bash
     pip install -r requirements.txt
     ```

3. **Struktur Direktori Proyek**:
   - Buat struktur direktori proyek seperti berikut:
     ```
     submission
     ├───model
     ├───data
     ├───notebook.ipynb
     ├───prediction.py
     ├───README.md
     ├───<username_dicoding>-dashboard.png (dapat lebih dari 1)
     ├───<username_dicoding>-video.mp4
     ├───metabase.db.mv.db (jika menggunakan metabase) / Book.twb (jika menggunakan tableu) 
     └───requirements.txt
     ```

4. **Menyiapkan Notebook Jupyter**:
   - Buka Jupyter Notebook atau Jupyter Lab dan buka file `notebook.ipynb`.
   - Lakukan analisis data, rekayasa fitur, pemodelan, dan evaluasi di dalam notebook ini.

5. **Menyiapkan File Prediksi**:
   - Buat file `prediction.py` untuk melakukan prediksi pada data baru menggunakan model yang telah dilatih.
   - Pastikan file `new_data.csv` tersedia dengan format yang sesuai untuk melakukan prediksi.

6. **Membuat Business Dashboard**:
   - Gunakan Tableau Public untuk membuat business dashboard berdasarkan hasil analisis.
   - Simpan screenshot dashboard dengan nama `<username_dicoding>-dashboard.png`.

7. **Dokumentasi Proyek**:
   - Pastikan semua langkah dan analisis terdokumentasi dengan baik di dalam `README.md` dan `notebook.ipynb`.

Dengan melakukan persiapan ini, Anda akan siap untuk melakukan analisis dan pemodelan data karyawan Jaya Jaya Maju serta menyusun business dashboard yang diperlukan.

## Business Dashboard

Business dashboard ini dibuat untuk membantu manajemen HR di Jaya Jaya Maju dalam memonitor dan menganalisis faktor-faktor yang mempengaruhi tingginya tingkat attrition karyawan. Dashboard ini dibuat menggunakan Tableau Public dan mencakup beberapa visualisasi yang memberikan wawasan mendalam mengenai data karyawan.

### Link Business Dashboard

1. **Analisa Fitur yang Mempengaruhi Attrition**:
   - Dashboard ini menampilkan fitur-fitur utama yang paling mempengaruhi keputusan karyawan untuk meninggalkan perusahaan. Visualisasi yang disertakan meliputi bar chart dari feature importance yang dihasilkan dari model machine learning.
   - Link: [Analisa Fitur yang Mempengaruhi Attrition](https://public.tableau.com/views/Book_17171328084740/HRAttritionAnalysisDashboard?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link)

2. **Hubungan antara Umur dan Pendapatan Bulanan yang Mempengaruhi Attrition**:
   - Dashboard ini menampilkan scatter plot yang menunjukkan hubungan antara umur dan pendapatan bulanan karyawan dengan status attrition yang disorot. Ini membantu mengidentifikasi apakah ada pola tertentu yang menunjukkan karyawan dengan karakteristik tertentu lebih mungkin untuk keluar.
   - Link: [Hubungan antara Umur dan Pendapatan Bulanan yang Mempengaruhi Attrition](https://public.tableau.com/views/Book_17170578411790/RelationBetweenAgeandMonthlyIncometoAttrition?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)

### Isi Dashboard

1. **Feature Importance Bar Chart**:
   - Menunjukkan fitur-fitur yang paling penting dalam memprediksi attrition karyawan berdasarkan model machine learning yang telah dilatih.
   - Visualisasi ini membantu manajemen HR untuk fokus pada faktor-faktor yang paling berpengaruh dalam pengambilan keputusan strategis.

2. **Scatter Plot: Umur vs Pendapatan Bulanan**:
   - Menampilkan hubungan antara umur karyawan dan pendapatan bulanan dengan status attrition yang di-highlight.
   - Visualisasi ini membantu mengidentifikasi kelompok karyawan tertentu yang mungkin memiliki risiko attrition lebih tinggi.

3. **Histogram Distribusi Usia**:
   - Menunjukkan distribusi usia karyawan yang keluar dan yang tetap di perusahaan.
   - Visualisasi ini memberikan wawasan mengenai rentang usia yang paling rentan terhadap attrition.

4. **Histogram Distribusi Pendapatan Bulanan**:
   - Menunjukkan distribusi pendapatan bulanan karyawan yang keluar dan yang tetap di perusahaan.
   - Visualisasi ini membantu mengidentifikasi rentang pendapatan yang paling rentan terhadap attrition.

Dashboard ini memberikan alat yang kuat bagi manajemen HR untuk memahami dan memantau faktor-faktor yang mempengaruhi attrition karyawan secara real-time. Dengan informasi ini, mereka dapat mengambil tindakan yang lebih terinformasi untuk meningkatkan retensi karyawan dan mengurangi tingkat attrition.

## Conclusion

Proyek ini berhasil menganalisis faktor-faktor yang mempengaruhi tingginya tingkat attrition di Jaya Jaya Maju dan menyediakan business dashboard untuk membantu manajemen HR dalam memantau dan mengambil tindakan yang diperlukan. Berikut adalah kesimpulan utama dari proyek ini:

1. **Identifikasi Faktor-faktor Utama yang Mempengaruhi Attrition**:
   - Analisis data karyawan menunjukkan bahwa faktor-faktor seperti umur, pendapatan bulanan, tarif harian, tarif bulanan, total tahun bekerja, dan tarif per jam memiliki pengaruh signifikan terhadap keputusan karyawan untuk keluar dari perusahaan.

2. **Model Prediksi Attrition**:
   - Model machine learning yang dilatih berhasil memprediksi attrition dengan tingkat akurasi yang cukup tinggi. Model ini menggunakan berbagai fitur penting yang diidentifikasi selama analisis data untuk membuat prediksi.

3. **Business Dashboard**:
   - Business dashboard yang dibuat menggunakan Tableau Public menyediakan visualisasi yang informatif dan mudah dipahami mengenai metrik-metrik penting terkait karyawan dan attrition. Dashboard ini mencakup:
     - Bar chart untuk menunjukkan feature importance.
     - Scatter plot untuk menampilkan hubungan antara umur dan pendapatan bulanan dengan attrition.
     - Histogram untuk distribusi usia karyawan.
     - Histogram untuk distribusi pendapatan bulanan karyawan.
   - Dashboard ini membantu manajemen HR dalam memantau dan menganalisis data karyawan secara real-time, sehingga memungkinkan pengambilan keputusan yang lebih terinformasi.

Dengan mengimplementasikan hasil analisis dan memanfaatkan business dashboard, Jaya Jaya Maju dapat mengurangi tingkat attrition karyawan dan menciptakan lingkungan kerja yang lebih stabil dan produktif. Proyek ini memberikan alat dan wawasan yang diperlukan bagi manajemen HR untuk mengambil tindakan yang tepat dalam mengelola karyawan mereka.

## Rekomendasi Action Items (Optional)

Berikut adalah beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka:

- **Menerapkan Jam Kerja Fleksibel**:
  - Implementasikan jam kerja fleksibel untuk meningkatkan keseimbangan kerja dan kehidupan karyawan. Fleksibilitas ini dapat membantu mengurangi stres dan meningkatkan kepuasan kerja, yang pada akhirnya dapat mengurangi tingkat attrition.

- **Meningkatkan Peluang Pengembangan Profesional**:
  - Tingkatkan peluang pelatihan dan pengembangan karier untuk meningkatkan kepuasan dan keterlibatan kerja karyawan. Program pelatihan yang efektif dapat membantu karyawan merasa lebih dihargai dan termotivasi untuk bertahan lebih lama di perusahaan.

- **Tinjauan Kompensasi yang Teratur**:
  - Secara teratur tinjau dan sesuaikan paket kompensasi agar tetap kompetitif dan adil. Kompensasi yang sesuai dengan pasar dapat membantu menarik dan mempertahankan karyawan berbakat, serta mengurangi risiko attrition.

Dengan melaksanakan action items ini, diharapkan Jaya Jaya Maju dapat meningkatkan retensi karyawan dan menciptakan lingkungan kerja yang lebih positif dan produktif.

