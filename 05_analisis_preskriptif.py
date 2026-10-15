"""
TAHAP 5 - ANALISIS PRESKRIPTIF
Pertanyaan: Langkah strategis apa yang sebaiknya diambil perusahaan?
"""
import pandas as pd
import matplotlib.pyplot as plt

from utils import (muat_data, atur_gaya, simpan_grafik, NAVY,
                   PALET_MEMBERSHIP, URUTAN_MEMBERSHIP)

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)

df = muat_data()
atur_gaya()

# 1) Nilai tiap segmen membership
hasil = df.groupby("Membership Type").agg(
    Jumlah_Pelanggan=("Customer ID", "count"),
    Rata_Rata_Spend=("Total Spend", "mean"),
    Rata_Rata_Items=("Items Purchased", "mean"),
    Rata_Rata_Rating=("Average Rating", "mean"),
).reindex(URUTAN_MEMBERSHIP).round(2)
print("=== Analisis berdasarkan membership ===")
print(hasil)

tertinggi = hasil["Rata_Rata_Spend"].idxmax()
print(f"\nMembership dengan rata-rata pengeluaran tertinggi: {tertinggi}")

g = hasil["Rata_Rata_Spend"]
fig, ax = plt.subplots(figsize=(6, 4.2))
ax.barh(g.index, g.values, color=[PALET_MEMBERSHIP[i] for i in g.index])
for i, v in enumerate(g.values):
    ax.text(v + 15, i, f"{v:,.0f}", va="center", color=NAVY, fontweight="bold")
ax.set_title("Rata-rata Pengeluaran per Membership")
ax.set_xlabel("Rata-rata Total Spend (USD)")
ax.set_xlim(0, g.max() + 170)
simpan_grafik("07_rata2_spend_membership.png")

# 2) Pelanggan pasif (> 30 hari sejak pembelian terakhir)
BATAS_HARI_PASIF = 30
pasif = df[df["Days Since Last Purchase"] > BATAS_HARI_PASIF]
print(f"\n=== Pelanggan pasif (> {BATAS_HARI_PASIF} hari) ===")
print(f"Jumlah: {len(pasif)} dari {len(df)} pelanggan ({len(pasif) / len(df):.0%})")
print(pasif["Membership Type"].value_counts().reindex(URUTAN_MEMBERSHIP))

# 3) Kepuasan per membership
print("\n=== Proporsi kepuasan per membership ===")
print(pd.crosstab(df["Membership Type"], df["Satisfaction Level"],
                  normalize="index").reindex(URUTAN_MEMBERSHIP).round(2))

# 4) Rekomendasi
rasio = g["Gold"] / g["Bronze"]
print("\n" + "=" * 60)
print("REKOMENDASI BISNIS")
print("=" * 60)
print(f"1. Dorong upgrade ke Gold: rata-rata spend Gold {rasio:.1f}x Bronze.")
print(f"2. Aktifkan kembali pelanggan pasif: {len(pasif)} pelanggan "
      f"> {BATAS_HARI_PASIF} hari, "
      f"{(pasif['Membership Type'] != 'Gold').sum()} di antaranya bukan Gold.")
print("3. Pertahankan pelanggan Gold lewat layanan prioritas dan loyalitas.")
print("4. Pantau kepuasan secara dini dengan model prediktif (data baru).")
