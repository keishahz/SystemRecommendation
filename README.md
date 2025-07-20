# Sistem Rekomendasi Kursus Online

**Nama:** Keisha Hernantya Zahra
**Sisters in Tech by RISTEK Fasilkom UI 2025**
**Machine Learning Operations - Portfolio Program**

---

## Deskripsi Proyek dan Pendekatan

Proyek ini bertujuan untuk membangun sebuah **sistem rekomendasi kursus online sederhana**. Sistem ini menggunakan data kursus yang telah di-scrape dari Class Central pada tugas sebelumnya. Pendekatan yang digunakan adalah **_Content-Based Filtering_**, di mana sistem akan merekomendasikan kursus berdasarkan kemiripan konten (judul) antar kursus. Tujuannya adalah membantu pengguna menemukan kursus lain yang relevan dengan kursus yang mereka minati.

---

## Penjelasan Proses Vektorisasi

### Metode yang Dipilih: TF-IDF (Term Frequency-Inverse Document Frequency)

Langkah krusial dalam proyek ini adalah mengubah teks judul kursus menjadi format numerik yang dapat dipahami oleh mesin. Untuk ini, saya memilih metode **TF-IDF**.

**Alasan Pemilihan Metode:**
1.  **Relevansi Kata Kunci:** TF-IDF sangat efektif dalam mengidentifikasi kata kunci yang paling penting dalam sebuah judul. Metode ini memberikan bobot tinggi pada kata-kata yang sering muncul di satu judul tetapi jarang muncul di judul-judul lainnya (misalnya, kata "django" atau "photoshop").
2.  **Mengurangi Bobot Kata Umum:** Sebaliknya, kata-kata yang sangat umum di semua dokumen (seperti "introduction" atau "course") akan diberikan bobot yang lebih rendah, sehingga tidak mendominasi proses perbandingan.
3.  **Kesesuaian dengan Tugas:** Untuk tugas merekomendasikan kursus berdasarkan kemiripan judul, pendekatan berbasis kata kunci seperti TF-IDF sangat cocok dan memberikan hasil yang intuitif serta mudah diinterpretasikan.

Prosesnya adalah dengan mengambil kolom `Cleaned Title` dari dataset, lalu mengubahnya menjadi matriks numerik menggunakan `TfidfVectorizer` dari library Scikit-learn.

---

## Penjelasan Hasil Rekomendasi

Setelah teks diubah menjadi vektor, kemiripan antar kursus dihitung menggunakan **Cosine Similarity**. Sistem kemudian dapat memberikan rekomendasi yang relevan berdasarkan skor kemiripan tertinggi.

Berikut adalah beberapa contoh hasil yang didapat:

* **Untuk kursus:** `CS50's Introduction to Computer Science`
    * **Rekomendasi yang diberikan:**
        1.  `Computer Science 101`
        2.  `CS101: Introduction to Computer Science I`
        3.  `An Introduction to Logic for Computer Science`
    * **Penjelasan:** Sistem berhasil mengidentifikasi kata kunci "Computer Science" dan merekomendasikan kursus lain dengan topik serupa, menunjukkan pemahaman kontekstual yang baik.

* **Untuk kursus:** `Introduction to Computer Science and Programming Using Python.`
    * **Rekomendasi yang diberikan:**
        1.  `CS50's Introduction to Artificial Intelligence with Python`
        2.  `Programming for Everybody (Getting Started with Python)`
        3.  `Learn to Program: The Fundamentals`
    * **Penjelasan:** Di sini, sistem mengenali pentingnya kata "Programming" dan "Python", sehingga memberikan rekomendasi kursus pemrograman lain yang juga menggunakan Python atau berfokus pada dasar-dasar pemrograman.

---

## Refleksi Singkat: Kendala dan Solusi

* **Kendala yang Ditemui:**
    Kendala utama yang saya temui adalah terjadinya `ValueError` saat mencoba menghasilkan rekomendasi untuk semua kursus secara serentak. Setelah diselidiki, error ini disebabkan oleh adanya **judul kursus yang duplikat** di dalam dataset. Hal ini membuat proses pencarian indeks menjadi ambigu dan menyebabkan kegagalan pada fungsi pengurutan skor kemiripan.

* **Cara Mengatasinya:**
    Solusinya adalah dengan memodifikasi fungsi `get_recommendations`. Saya menambahkan sebuah logika `if-else` untuk memeriksa apakah hasil pencarian indeks mengembalikan satu nilai atau beberapa (sebuah Series). Jika yang dikembalikan adalah Series (menandakan adanya duplikat), fungsi akan diinstruksikan untuk **hanya mengambil indeks pertama** yang ditemukan. Perbaikan kecil ini berhasil mengatasi error dan membuat proses berjalan lancar untuk keseluruhan dataset.
