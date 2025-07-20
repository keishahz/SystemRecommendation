import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Membaca dataset dari file CSV
file_name = '/content/classcentral.csv'
df = pd.read_csv(file_name)

# Mengisi nilai kosong pada kolom 'Cleaned Title' dengan string kosong
course_titles_cleaned = df['Cleaned Title'].fillna('')

# Membuat vektor TF-IDF dari teks judul kursus
vectorizer = TfidfVectorizer(stop_words='english')  # Menghilangkan stop words bahasa Inggris
tfidf_matrix = vectorizer.fit_transform(course_titles_cleaned)  # Hasil: matriks dokumen-term

# Menghitung kemiripan antar kursus menggunakan cosine similarity
cosine_sim_matrix = cosine_similarity(tfidf_matrix)

# Membuat Series untuk mencari indeks kursus berdasarkan judul
indices = pd.Series(df.index, index=df['Title'])

def get_recommendations(title, top_n=5):
    """
    Fungsi rekomendasi berdasarkan kemiripan judul kursus.
    Akan mengembalikan daftar kursus serupa.
    """

    try:
        # Mencari indeks dari judul kursus
        idx_lookup = indices[title]

        # Menangani kasus jika ada duplikat judul
        if isinstance(idx_lookup, pd.Series):
            idx = idx_lookup.iloc[0]  # Ambil indeks pertama saja
        else:
            idx = idx_lookup

    except KeyError:
        # Jika judul tidak ditemukan dalam data
        return f"Kursus dengan judul '{title}' tidak ditemukan."

    # Mengambil skor kemiripan dari matriks cosine
    sim_scores = list(enumerate(cosine_sim_matrix[idx]))  # List berisi indeks dan skor similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  # Urutkan dari paling mirip
    sim_scores = sim_scores[1:top_n+1]  # Ambil top-N (lewatkan indeks sendiri)
    course_indices = [i[0] for i in sim_scores]  # Ambil hanya indeks kursus

    # Kembalikan judul-judul yang direkomendasikan
    return df['Title'].iloc[course_indices]

print("✅ Fungsi 'get_recommendations' yang sudah diperbaiki telah siap.")

# --- Menguji Fungsi Rekomendasi ---
# Mengambil judul kursus pertama untuk uji coba
target_course_title = df['Title'].iloc[0]

print(f"--- Rekomendasi untuk: '{target_course_title}' ---")
recommendations = get_recommendations(target_course_title, top_n=5)
print(recommendations)
print("-" * 50)

# --- Membuat File Hasil untuk Semua Judul ---
print("\nMembuat file hasil untuk semua kursus...")

all_recommendations = {}
for title in df['Title']:
    # Ambil 3 rekomendasi teratas untuk setiap judul kursus
    recs = get_recommendations(title, top_n=3)

    # Simpan hasil dalam dictionary
    if isinstance(recs, pd.Series):
        all_recommendations[title] = recs.tolist()
    else:
        all_recommendations[title] = []  # Jika tidak ada rekomendasi

# Mengubah dictionary ke bentuk DataFrame
recs_df = pd.DataFrame.from_dict(
    all_recommendations,
    orient='index',
    columns=['Recommendation_1', 'Recommendation_2', 'Recommendation_3']
)
recs_df.index.name = 'Course_Title'

# Menyimpan DataFrame ke file CSV
output_filename = 'course_recommendations.csv'
recs_df.to_csv(output_filename)

print(f"✅ File hasil '{output_filename}' berhasil dibuat!")
print("Semua langkah coding sudah selesai. Anda sekarang siap untuk menyusun laporan dan mengunggahnya ke GitHub.")
