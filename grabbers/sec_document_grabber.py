import requests
import os
import html2text
import re

# Set User-Agent header for SEC API
HEADERS = {"User-Agent": "YourAppName/1.0 (contact@yourdomain.com)"}

def get_cik(ticker):
    """
    Fetch the CIK for a given ticker from SEC's company_tickers.json.
    """
    url = "https://www.sec.gov/files/company_tickers.json"
    response = requests.get(url, headers=HEADERS)
    tickers = response.json()
    for entry in tickers.values():
        if entry["ticker"].upper() == ticker.upper():
            return str(entry["cik_str"]).zfill(10)
    return None

def get_quarterly_filing_url(cik, year, quarter):
    """
    Fetch the 10-Q filings for a specific CIK, year, and quarter.
    """
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    response = requests.get(url, headers=HEADERS)
    filings = response.json().get("filings", {}).get("recent", {})
    
    for form, date, document, accession in zip(
        filings["form"], filings["filingDate"], filings["primaryDocument"], filings["accessionNumber"]
    ):
        if form == "10-Q" and date.startswith(str(year)):
            # Build the URL for the filing
            filing_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession.replace('-', '')}/{document}"
            return filing_url
    return None

def get_10q_filing(ticker, year, quarter):
    """
    Main function to get the 10-Q filing URL given ticker, year, and quarter.
    """
    print(f"Fetching CIK for ticker: {ticker}")
    cik = get_cik(ticker)
    if not cik:
        return f"Error: Ticker '{ticker}' not found."
    
    print(f"Fetching 10-Q filing for {ticker} ({cik}) in {year}-Q{quarter}")
    filing_url = get_quarterly_filing_url(cik, year, quarter)
    if filing_url:
        return f"10-Q Filing URL: {filing_url}"
    else:
        return f"Error: No 10-Q filing found for {ticker} in {year}-Q{quarter}."

def save_filing(url, ticker, year, quarter):
    """
    Download and save the 10-Q filing from the given URL.
    """
    print(f"Downloading 10-Q filing from {url}...")
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        dir_path = os.path.join("data", ticker, str(year), f"Q{quarter}")
        os.makedirs(dir_path, exist_ok=True)  # Ensure directory exists
        filename = f"{ticker}_{year}_Q{quarter}_10Q.html"
        filepath = os.path.join(dir_path, filename)
        with open(filepath, "wb") as file:
            file.write(response.content)
        print(f"File saved as: {filepath}")
        return filepath
    else:
        print(f"Failed to download filing. HTTP Status Code: {response.status_code}")
        return None

def clean_html(html_content):
    # Remove comments
    cleaned_content = re.sub(r'<!--.*?-->', '', html_content, flags=re.DOTALL)
    # Remove extra whitespace
    cleaned_content = re.sub(r'\s+', ' ', cleaned_content)
    # Remove unnecessary tags (e.g., <div>, <span> with no attributes)
    cleaned_content = re.sub(r'<(div|span)[^>]*?>\s*</\1>', '', cleaned_content)
    return cleaned_content

def convert_html_to_markdown(html_filepath):
    """
    Convert the HTML file to a clean markdown document.
    """
    with open(html_filepath, "r", encoding="utf-8") as html_file:
        html_content = html_file.read()
    
    html_content = clean_html(html_content)
    markdown_content = html2text.html2text(html_content)
    
    markdown_filepath = html_filepath.replace(".html", ".md")
    with open(markdown_filepath, "w", encoding="utf-8") as markdown_file:
        markdown_file.write(markdown_content)
    
    print(f"Markdown file saved as: {markdown_filepath}")
    return markdown_filepath

def create_human_readable_markdown(markdown_filepath):
    """
    Create a reduced human-readable version of the markdown document.
    """
    with open(markdown_filepath, "r", encoding="utf-8") as markdown_file:
        markdown_content = markdown_file.readlines()
    
    # Simple heuristic to filter out less relevant lines
    human_readable_content = []
    for line in markdown_content:
        if not line.startswith("#") and len(line.strip()) > 0:
            human_readable_content.append(line)
    
    human_readable_filepath = markdown_filepath.replace(".md", "_trimmed.md")
    with open(human_readable_filepath, "w", encoding="utf-8") as human_readable_file:
        human_readable_file.writelines(human_readable_content)
    
    print(f"Human-readable markdown file saved as: {human_readable_filepath}")

def process_10q_filing(ticker, year, quarter):
    """
    Process the 10-Q filing for a given ticker, year, and quarter.
    """
    filing_url = get_10q_filing(ticker, year, quarter)
    print(filing_url)
    if "10-Q Filing URL:" in filing_url:
        filing_url = filing_url.replace("10-Q Filing URL: ", "")
        html_filepath = save_filing(filing_url, ticker, year, quarter)
        if html_filepath:
            markdown_filepath = convert_html_to_markdown(html_filepath)
            create_human_readable_markdown(markdown_filepath)
    else:
        print(filing_url)

if __name__ == "__main__":
    ticker = "AAPL"
    year = 2024
    quarter = 2
    process_10q_filing(ticker, year, quarter)