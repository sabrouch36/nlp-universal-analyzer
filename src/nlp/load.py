# Auto-generated file
from pathlib import Path

import pandas as pd


def run_load(df: pd.DataFrame, output_path: Path):
    """Save DataFrame to CSV."""

    print("🔹 Saving data...")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"✅ Data saved to: {output_path}")
