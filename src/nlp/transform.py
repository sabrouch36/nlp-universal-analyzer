# Auto-generated file
import re
import string
from bs4 import BeautifulSoup
import pandas as pd


def clean_text(text: str) -> str:
    """Clean text for NLP analysis."""

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


def run_transform(soup: BeautifulSoup) -> pd.DataFrame:
    """Extract and transform text into structured data."""

    print("🔹 Transforming data...")

    # Extract text (generic approach)
    paragraphs = soup.find_all("p")
    raw_text = " ".join([p.get_text() for p in paragraphs])

    if not raw_text:
        raw_text = "No text found"

    # Clean text
    clean = clean_text(raw_text)

    # Tokenization
    tokens = clean.split()

    # Metrics
    token_count = len(tokens)
    unique_token_count = len(set(tokens))
    type_token_ratio = round(unique_token_count / token_count, 4) if token_count > 0 else 0

    # Build DataFrame
    data = {
        "raw_text": raw_text[:500],  # shortened for readability
        "clean_text": clean[:500],
        "token_count": token_count,
        "unique_token_count": unique_token_count,
        "type_token_ratio": type_token_ratio,
        "tokens": " ".join(tokens[:50])
    }

    df = pd.DataFrame([data])

    print("✅ Transformation complete")

    return df