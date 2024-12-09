import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set User-Agent header for the API
HEADERS = {"User-Agent": "YourAppName/1.0 (contact@yourdomain.com)"}

def get_transcript(ticker, quarter, year):
    """
    Fetch the earnings transcript for a given ticker, quarter, and year.
    """
    url = f"https://discountingcashflows.com/api/transcript/{ticker}/Q{quarter}/{year}/"
    api_key = os.getenv("DCF_API_KEY")
    response = requests.get(url, headers=HEADERS, auth=("user", api_key))
    return response

def save_transcript(response, ticker, year, quarter):
    """
    Save the transcript to a file.
    """
    dir_path = os.path.join("data", ticker, str(year), f"Q{quarter}")
    os.makedirs(dir_path, exist_ok=True)  # Ensure directory exists
    filename = f"{ticker}_{year}_Q{quarter}_meeting_transcript.json"
    filepath = os.path.join(dir_path, filename)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(response.text)
    print(f"Transcript saved as: {filepath}")
    return filepath

def process_transcript(ticker, quarter, year):
    """
    Process the earnings transcript for a given ticker, quarter, and year.
    """
    response = get_transcript(ticker, quarter, year)
    print(response)
    print(response.text)
    save_transcript(response, ticker, year, quarter)

if __name__ == "__main__":
    ticker = "AAPL"
    quarter = 2
    year = 2024
    process_transcript(ticker, quarter, year)