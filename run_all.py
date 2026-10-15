"""Menjalankan kelima tahap analisis secara berurutan (tanpa jendela grafik)."""
import os
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
SCRIPTS = [
    "01_analisis_deskriptif.py",
    "02_eda.py",
    "03_model_mekanistik.py",
    "04_analisis_prediktif.py",
    "05_analisis_preskriptif.py",
]

env = dict(os.environ, MPLBACKEND="Agg")  # simpan grafik saja, tanpa pop-up
for nama in SCRIPTS:
    print("\n" + "#" * 70 + f"\n# {nama}\n" + "#" * 70)
    subprocess.run([sys.executable, str(BASE / nama)], check=True, cwd=BASE, env=env)
print("\nSelesai. Semua grafik ada di folder output/.")
