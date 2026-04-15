# Auto-generated file
from bs4 import BeautifulSoup


def run_validate(html_content: str) -> BeautifulSoup:
    """Validate and parse HTML content."""

    print("🔹 Validating HTML structure...")

    soup = BeautifulSoup(html_content, "html.parser")

    # Basic validation checks
    title = soup.find("h1")
    paragraphs = soup.find_all("p")

    print(f"Title found: {title is not None}")
    print(f"Paragraphs found: {len(paragraphs)}")

    if not title:
        print("⚠️ Warning: No title found")

    if len(paragraphs) == 0:
        print("⚠️ Warning: No paragraph content found")

    print("✅ Validation complete")

    return soup