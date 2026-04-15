# Auto-generated file
from pathlib import Path

# ============================================================
# 🌐 DATA SOURCE CONFIGURATION
# ============================================================

# You can change this URL anytime (this is the power of the system)
PAGE_URL: str = "https://arxiv.org/abs/2401.00001"

HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (NLP Universal Analyzer - educational project)"
}

# ============================================================
# 📁 PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()

DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

RAW_HTML_PATH: Path = RAW_PATH / "raw.html"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "processed.csv"