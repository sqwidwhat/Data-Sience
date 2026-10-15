"""
TAHAP 1 - ANALISIS DESKRIPTIF
Pertanyaan: Apa yang terjadi? Bagaimana profil pelanggan dan kaitannya
dengan tipe membership?
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utils import (muat_data, atur_gaya, simpan_grafik, KOLOM_NUMERIK,
                   PALET_MEMBERSHIP, URUTAN_MEMBERSHIP)

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)

df = muat_data()
atur_gaya()

print("=== Ukuran dataset ===")
print(f"{df.shape[0]} pelanggan, {df.shape[1]} variabel")

print("\n=== Statistik deskriptif ===")
print(df[KOLOM_NUMERIK].describe().round(2))

print("\n=== Jumlah pelanggan per tipe membership ===")
print(df["Membership Type"].value_counts())

print("\n=== Ringkasan per tipe membership ===")
ringkasan = df.groupby("Membership Type").agg(
    Jumlah=("Customer ID", "count"),
    Rata2_Spend=("Total Spend", "mean"),
    Median_Spend=("Total Spend", "median"),
    Min_Spend=("Total Spend", "min"),
    Maks_Spend=("Total Spend", "max"),
    Rata2_Item=("Items Purchased", "mean"),
    Rata2_Rating=("Average Rating", "mean"),
    Rata2_Hari_Sejak_Beli=("Days Since Last Purchase", "mean"),
    Rata2_Usia=("Age", "mean"),
).reindex(URUTAN_MEMBERSHIP).round(2)
print(ringkasan)

gold, bronze = ringkasan.loc["Gold", "Rata2_Spend"], ringkasan.loc["Bronze", "Rata2_Spend"]
print(f"\nInsight: rata-rata spend Gold {gold / bronze:.1f}x lebih besar dari Bronze.")

# Visualisasi: boxplot Total Spend per membership
fig, ax = plt.subplots(figsize=(6, 4.2))
sns.boxplot(x="Membership Type", y="Total Spend", data=df,
            order=URUTAN_MEMBERSHIP, hue="Membership Type",
            palette=PALET_MEMBERSHIP, legend=False, ax=ax)
ax.set_title("Total Spend per Tipe Membership")
ax.set_xlabel("Tipe Membership")
ax.set_ylabel("Total Spend (USD)")
simpan_grafik("01_boxplot_spend_membership.png")
