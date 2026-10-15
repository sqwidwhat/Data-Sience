# Paket Analisis Data Science: Perilaku Pelanggan E-Commerce

Paket kode lengkap di balik presentasi **Analisis_Perilaku_Pelanggan_E-Commerce.pptx**.
Dataset: 350 pelanggan, 11 variabel (usia, kota, tipe membership, total spend,
jumlah item, rating, diskon, hari sejak pembelian terakhir, tingkat kepuasan).

## Struktur Folder

```
paket_analisis_data_science/
├── dataset/
│   └── E-commerce Customer Behavior - Sheet1.csv
├── 01_analisis_deskriptif.py     (Slide 3)
├── 02_eda.py                     (Slide 4)
├── 03_model_mekanistik.py        (Slide 5)
├── 04_analisis_prediktif.py      (Slide 6)
├── 05_analisis_preskriptif.py    (Slide 7)
├── utils.py                      (fungsi bantu: baca data, gaya & simpan grafik)
├── run_all.py                    (jalankan semua tahap sekaligus)
├── requirements.txt
├── output/                       (grafik hasil; dibuat ulang saat script dijalankan)
└── Analisis_Perilaku_Pelanggan_E-Commerce.pptx
```

## Cara Menjalankan

Butuh Python 3.9 atau lebih baru.

```bash
# 1. (opsional) buat virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS / Linux

# 2. pasang library
pip install -r requirements.txt

# 3a. jalankan semua tahap sekaligus (grafik hanya disimpan ke output/)
python run_all.py

# 3b. atau jalankan satu tahap (grafik tampil di jendela dan tersimpan)
python 01_analisis_deskriptif.py
```

Jalankan perintah dari dalam folder ini agar import `utils.py` berfungsi.

## Ringkasan Tahap Analisis

| Tahap | Script | Pertanyaan | Temuan Utama |
|---|---|---|---|
| 1. Deskriptif | `01_...` | Apa yang terjadi? | Rata-rata usia 33,6 th, spend $845; Gold $1.311 vs Bronze $473 (±2,8x) |
| 2. EDA | `02_...` | Pola apa yang muncul? | Items vs spend r = 0,97; rating vs spend r = 0,94 |
| 3. Mekanistik | `03_...` | Bagaimana dinamikanya? | Model dP/dt = k(P̄ − P), k = 0,8 (asumsi), konvergen ke rata-rata |
| 4. Prediktif | `04_...` | Bisakah kepuasan diprediksi? | Random Forest, akurasi 100% (data uji 70); fitur teratas: hari sejak beli terakhir |
| 5. Preskriptif | `05_...` | Apa yang harus dilakukan? | Upgrade ke Gold, aktivasi pelanggan pasif, retensi Gold, pantau kepuasan |

## Catatan Penting

- **Akurasi 100%** pada data kecil perlu diwaspadai: kepuasan sangat terkait tipe
  membership (semua pelanggan Gold berstatus Satisfied). Validasi dengan data baru.
- **2 baris tanpa label kepuasan** otomatis dikeluarkan pada tahap prediktif
  (348 dari 350 baris dipakai).
- **Model mekanistik** bersifat ilustratif. Nilai k = 0,8 adalah asumsi, bukan hasil
  estimasi dari data. Titik awal 1.500 ditambahkan sebagai pembanding terhadap
  titik awal 400.
- **Korelasi bukan sebab-akibat.** Hubungan pada tahap EDA tidak membuktikan kausalitas.
- Mata uang tidak tercantum pada dataset; simbol "$" dipakai karena kota-kotanya
  berada di Amerika Serikat.
- Hasil Random Forest dapat berbeda tipis bila versi scikit-learn berbeda
  (`random_state=42` sudah ditetapkan).
