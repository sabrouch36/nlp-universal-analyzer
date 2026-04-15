# Auto-generated file
import requests
from pathlib import Path


def run_extract(url: str, headers: dict, output_path: Path) -> str:
    """Fetch HTML content from a web page and save it."""

    print("🔹 Extracting data from URL...")
    print(f"URL: {url}")

    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    html_content = response.text

    # Save raw HTML
    output_path.write_text(html_content, encoding="utf-8")

    print(f"✅ HTML saved to: {output_path}")

    return html_content