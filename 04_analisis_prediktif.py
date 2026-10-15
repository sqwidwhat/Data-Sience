"""
TAHAP 4 - ANALISIS PREDIKTIF
Pertanyaan: Bisakah tingkat kepuasan pelanggan diprediksi, dan variabel apa
yang paling berpengaruh?
Model: Random Forest Classifier.
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from utils import muat_data, atur_gaya, simpan_grafik, KOLOM_NUMERIK, TEAL, AMBER, GREY

pd.set_option("display.width", 200)

df = muat_data()
atur_gaya()

print("=== Distribusi Satisfaction Level ===")
print(df["Satisfaction Level"].value_counts(dropna=False))

# Grafik distribusi kepuasan
fig, ax = plt.subplots(figsize=(5.6, 4.2))
hitung = df["Satisfaction Level"].value_counts().reindex(["Satisfied", "Neutral", "Unsatisfied"])
ax.bar(hitung.index, hitung.values, color=[TEAL, GREY, AMBER])
for i, v in enumerate(hitung.values):
    ax.text(i, v + 2, str(v), ha="center", fontweight="bold")
ax.set_title("Distribusi Tingkat Kepuasan")
ax.set_ylabel("Jumlah Pelanggan")
simpan_grafik("05_distribusi_kepuasan.png")

# Persiapan data (baris tanpa label kepuasan dibuang)
fitur = KOLOM_NUMERIK
data = df[fitur + ["Satisfaction Level"]].dropna()
print(f"\nData dipakai: {len(data)} dari {len(df)} baris "
      f"({len(df) - len(data)} baris tanpa label dikeluarkan)")

X = data[fitur]
encoder = LabelEncoder()
y = encoder.fit_transform(data["Satisfaction Level"])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Melatih dan mengevaluasi model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
prediksi = model.predict(X_test)

print(f"\nAkurasi pada {len(y_test)} data uji: {accuracy_score(y_test, prediksi):.3f}")
print("\nClassification report:")
print(classification_report(y_test, prediksi, target_names=encoder.classes_, zero_division=0))
print("Confusion matrix (baris = aktual, kolom = prediksi):")
print(pd.DataFrame(confusion_matrix(y_test, prediksi),
                   index=encoder.classes_, columns=encoder.classes_))

print("\nPERHATIAN: akurasi sempurna pada data kecil perlu diwaspadai. "
      "Kepuasan sangat terkait tipe membership, sehingga model perlu "
      "divalidasi dengan data baru.")

# Tingkat kepentingan fitur
pentingnya = pd.Series(model.feature_importances_, index=fitur).sort_values()
print("\nTingkat kepentingan fitur:")
print(pentingnya.sort_values(ascending=False).round(3))

label = {"Age": "Usia", "Total Spend": "Total Spend", "Items Purchased": "Item Dibeli",
         "Average Rating": "Rating Rata-rata", "Days Since Last Purchase": "Hari Sejak Beli Terakhir"}
fig, ax = plt.subplots(figsize=(6.4, 4.2))
warna = [AMBER if v == pentingnya.max() else TEAL for v in pentingnya.values]
ax.barh([label[i] for i in pentingnya.index], pentingnya.values, color=warna)
for i, v in enumerate(pentingnya.values):
    ax.text(v + 0.005, i, f"{v:.2f}", va="center", fontsize=10)
ax.set_title("Tingkat Kepentingan Fitur")
ax.set_xlabel("Nilai Kepentingan")
ax.set_xlim(0, pentingnya.max() + 0.08)
simpan_grafik("06_kepentingan_fitur.png")

# Insight pendukung: keaktifan vs kepuasan
print("\nRata-rata hari sejak pembelian terakhir per tingkat kepuasan:")
print(df.groupby("Satisfaction Level")["Days Since Last Purchase"].mean().round(1))
