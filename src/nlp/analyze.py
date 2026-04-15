# Auto-generated file
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud


def run_analyze(df: pd.DataFrame, output_dir: Path):
    """Analyze text and create visualizations."""

    print("🔹 Analyzing data...")

    output_dir.mkdir(parents=True, exist_ok=True)

    # Get tokens
    tokens_str = df.iloc[0]["tokens"]
    tokens = tokens_str.split()

    if not tokens:
        print("⚠️ No tokens found")
        return

    # =========================
    # Top tokens (bar chart)
    # =========================
    counter = Counter(tokens)
    top = counter.most_common(10)

    words = [w for w, c in top]
    counts = [c for w, c in top]

    plt.figure(figsize=(8, 5))
    plt.barh(words[::-1], counts[::-1])
    plt.title("Top Tokens")
    plt.xlabel("Frequency")
    plt.tight_layout()

    bar_path = output_dir / "top_tokens.png"
    plt.savefig(bar_path)
    plt.close()

    print(f"✅ Saved bar chart: {bar_path}")

    # =========================
    # WordCloud
    # =========================
    wc = WordCloud(width=800, height=400, background_color="white")
    wc.generate(tokens_str)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc)
    plt.axis("off")

    wc_path = output_dir / "wordcloud.png"
    plt.savefig(wc_path)
    plt.close()

    print(f"✅ Saved wordcloud: {wc_path}")

    print("✅ Analysis complete")
