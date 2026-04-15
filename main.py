# Auto-generated file
from src.nlp.config import PAGE_URL, HEADERS, RAW_HTML_PATH, PROCESSED_CSV_PATH
from src.nlp.extract import run_extract
from src.nlp.validate import run_validate
from src.nlp.transform import run_transform
from src.nlp.analyze import run_analyze
from src.nlp.load import run_load
from pathlib import Path


def main():
    print("🚀 Starting NLP Universal Analyzer...")

    # Step 1: Extract
    html = run_extract(PAGE_URL, HEADERS, RAW_HTML_PATH)

    # Step 2: Validate
    soup = run_validate(html)

    # Step 3: Transform
    df = run_transform(soup)

    # Step 4: Analyze
    run_analyze(df, Path("data/processed"))

    # Step 5: Load
    run_load(df, PROCESSED_CSV_PATH)

    print("🎉 Pipeline completed successfully!")


if __name__ == "__main__":
    main()