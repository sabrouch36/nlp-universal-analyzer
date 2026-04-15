# nlp-universal-analyzer
Reusable NLP pipeline for extracting, cleaning, and analyzing text from web pages using Python
# 🚀 NLP Universal Analyzer

A reusable Natural Language Processing (NLP) pipeline for extracting, cleaning, and analyzing text from web pages using Python.

---

## 📌 Overview

This project demonstrates a complete NLP workflow that transforms raw web data into structured insights.

The pipeline follows a professional EVTL architecture:

- Extract → Fetch HTML from a web page  
- Validate → Parse and inspect structure  
- Transform → Clean text and generate features  
- Analyze → Visualize patterns and insights  
- Load → Save results for reuse  

---

## ⚙️ Features

- 🌐 Extract text from any web page
- 🧠 Clean and normalize text data
- 🔤 Tokenization and word analysis
- 📊 Frequency analysis of top words
- ☁️ WordCloud visualization
- 📁 Export results to CSV
- 🔁 Fully reusable pipeline (just change the URL)

---

## 🧱 Project Structure
nlp-universal-analyzer/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── src/
│ └── nlp/
│ ├── config.py
│ ├── extract.py
│ ├── validate.py
│ ├── transform.py
│ ├── analyze.py
│ └── load.py
│
└── main.py


---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/sabrouch36/nlp-universal-analyzer.git
cd nlp-universal-analyzer
2. Install dependencies
pip install requests beautifulsoup4 pandas matplotlib wordcloud
3. Run the pipeline
python main.py
📊 Output

After running the pipeline, results will be saved in:

data/processed/
processed.csv → structured dataset
top_tokens.png → most frequent words
wordcloud.png → visual representation of text
🔧 Customization

To analyze a different web page, simply change the URL in:

src/nlp/config.py
PAGE_URL = "your_new_url_here"
🧠 Skills Demonstrated
Python data processing
Web scraping (HTML parsing)
Natural Language Processing (NLP)
Data cleaning and normalization
Feature engineering
Data visualization
Pipeline architecture (EVTL)
🏆 Author

Sabri Hamdaoui

⭐ Final Note

This project demonstrates how unstructured web data can be transformed into meaningful insights using a structured and reusable NLP pipeline.