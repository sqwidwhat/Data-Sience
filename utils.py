"""Fungsi bantu bersama untuk seluruh script analisis."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "dataset" / "E-commerce Customer Behavior - Sheet1.csv"
OUTPUT_DIR = BASE_DIR / "output"

# Palet warna konsisten dengan presentasi
NAVY, TEAL, AMBER, GREY = "#12304A", "#1B8A8F", "#F2B21A", "#6B7785"
PALET_MEMBERSHIP = {"Bronze": "#9C5B2E", "Silver": "#9AA7B4", "Gold": AMBER}
URUTAN_MEMBERSHIP = ["Bronze", "Silver", "Gold"]

KOLOM_NUMERIK = ["Age", "Total Spend", "Items Purchased",
                 "Average Rating", "Days Since Last Purchase"]


def muat_data() -> pd.DataFrame:
    """Membaca dataset e-commerce (350 pelanggan, 11 variabel)."""
    return pd.read_csv(DATA_PATH)


def atur_gaya() -> None:
    plt.rcParams.update({
        "axes.edgecolor": "#CBD2D9", "axes.labelcolor": NAVY,
        "xtick.color": GREY, "ytick.color": GREY,
        "axes.titleweight": "bold", "axes.titlecolor": NAVY,
        "axes.spines.top": False, "axes.spines.right": False,
    })


def simpan_grafik(nama_file: str) -> None:
    """Menyimpan grafik ke folder output/ lalu menampilkannya."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / nama_file, dpi=200, facecolor="white")
    print(f"[grafik tersimpan] output/{nama_file}")
    plt.show()
    plt.close()
