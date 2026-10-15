"""
TAHAP 2 - EXPLORATORY DATA ANALYSIS (EDA)
Pertanyaan: Pola dan hubungan apa yang ada antar variabel?
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

from utils import (muat_data, atur_gaya, simpan_grafik, KOLOM_NUMERIK,
                   NAVY, TEAL, PALET_MEMBERSHIP, URUTAN_MEMBERSHIP)

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)

df = muat_data()
atur_gaya()

print("=== Data kosong per kolom ===")
print(df.isna().sum()[df.isna().sum() > 0])

print("\n=== Kemencengan (skewness) Total Spend ===")
print(round(stats.skew(df["Total Spend"]), 2), "(positif = condong ke kanan)")

print("\n=== Matriks korelasi ===")
korelasi = df[KOLOM_NUMERIK].corr().round(2)
print(korelasi)

print("\nKorelasi kunci terhadap Total Spend:")
for kolom in ["Items Purchased", "Average Rating", "Age", "Days Since Last Purchase"]:
    print(f"  Total Spend vs {kolom}: r = {korelasi.loc['Total Spend', kolom]}")

# 1) Histogram distribusi Total Spend
fig, ax = plt.subplots(figsize=(6, 4.2))
sns.histplot(data=df, x="Total Spend", kde=True, color=TEAL, ax=ax)
ax.set_title("Distribusi Total Spend")
ax.set_xlabel("Total Spend (USD)")
ax.set_ylabel("Jumlah Pelanggan")
simpan_grafik("02_histogram_total_spend.png")

# 2) Scatter plot Items Purchased vs Total Spend
fig, ax = plt.subplots(figsize=(6, 4.2))
sns.scatterplot(data=df, x="Items Purchased", y="Total Spend",
                hue="Membership Type", hue_order=URUTAN_MEMBERSHIP,
                palette=PALET_MEMBERSHIP, s=45, ax=ax)
ax.set_title("Items Purchased vs Total Spend")
ax.set_xlabel("Jumlah Item Dibeli")
ax.set_ylabel("Total Spend (USD)")
ax.legend(title="Membership", frameon=False)
simpan_grafik("03_scatter_items_vs_spend.png")

# 3) Heatmap korelasi (tambahan)
fig, ax = plt.subplots(figsize=(6.4, 5))
sns.heatmap(korelasi, annot=True, cmap="crest", vmin=-1, vmax=1, ax=ax)
ax.set_title("Matriks Korelasi Variabel Numerik")
simpan_grafik("03b_heatmap_korelasi.png")

print("\nCatatan: korelasi menunjukkan hubungan, bukan sebab-akibat.")
