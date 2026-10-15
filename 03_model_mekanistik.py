"""
TAHAP 3 - MODEL MEKANISTIK
Pertanyaan: Bagaimana dinamika pengeluaran pelanggan jika kita memodelkannya
dengan mekanisme sederhana?

Persamaan diferensial:  dP/dt = k * (P_rata - P)
  P       : pengeluaran pelanggan
  P_rata  : rata-rata Total Spend seluruh pelanggan (dari data)
  k       : laju penyesuaian (ASUMSI = 0,8, bukan hasil estimasi data)

Logika: makin jauh pengeluaran dari rata-rata, makin cepat ia bergerak
mendekatinya. Model ini bersifat ilustratif dan perlu divalidasi dengan
data historis (time series) sebelum dipakai untuk keputusan.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from utils import muat_data, atur_gaya, simpan_grafik, NAVY, TEAL, AMBER

df = muat_data()
atur_gaya()

P_RATA = df["Total Spend"].mean()
K = 0.8


def model(P, t, k, p_rata):
    return k * (p_rata - P)


t = np.linspace(0, 10, 100)

fig, ax = plt.subplots(figsize=(6.4, 4.2))
for p0, warna in [(400, TEAL), (1500, AMBER)]:
    P = odeint(model, p0, t, args=(K, P_RATA)).ravel()
    # waktu saat selisih dengan rata-rata < 1% dari selisih awal
    ambang = abs(p0 - P_RATA) * 0.01
    idx = np.argmax(np.abs(P - P_RATA) < ambang)
    print(f"Titik awal {p0:>5}: mencapai 99% jarak ke rata-rata "
          f"(${P_RATA:,.0f}) pada t = {t[idx]:.1f}")
    ax.plot(t, P, color=warna, lw=2.5, label=f"Awal {p0}")

ax.axhline(P_RATA, color=NAVY, ls="--", lw=1.2)
ax.text(7.2, P_RATA + 30, f"Rata-rata {P_RATA:,.0f}", color=NAVY, fontsize=10)
ax.set_title("Simulasi Pengeluaran Menuju Rata-rata")
ax.set_xlabel("Waktu Simulasi")
ax.set_ylabel("Total Spend (USD)")
ax.legend(frameon=False)
simpan_grafik("04_simulasi_model_mekanistik.png")
