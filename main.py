import json
from grabbers.transcript_grabber import process_transcript
from grabbers.sec_document_grabber import process_10q_filing

if __name__ == "__main__":
    with open("grabber_settings.json", "r") as file:
        settings = json.load(file)
    
    tickers = settings["tickers"]
    years = settings["years"]
    quarters = settings["quarters"]
    
    for ticker in tickers:
        for year in years:
            for quarter in quarters:
                print(f"Processing earnings transcript for {ticker}, Q{quarter} {year}...")
                process_transcript(ticker, quarter, year)
                
                print(f"Processing 10-Q filing for {ticker}, Q{quarter} {year}...")
                process_10q_filing(ticker, year, quarter)