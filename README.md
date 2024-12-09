grab the transcript and associated SEC document filing of a given company's quarterly earnings report.

1. dependencies:
- `python3`
- `pip3 install requests html2text python-dotenv`

2. api_keys:
- grab an API key from [discountedcashflow.com] for the transcripts (free for now, until January 15th 2025, apptly)
- copy `.env.example` to a new file and rename it to `.env`
- insert the API key after `DCF_API_KEY=`

3. set up the `grabber_settings.json` to determine which ticker companies, years, and quarters you want to pull down. Default example:

```json
{
    "tickers": ["AAPL", "MSFT", "GOOGL"],
    "years": [2023, 2024],
    "quarters": [1, 2, 3, 4]
}
```
4. run:
- `python3 main.py`

5. output
- generates files in the `data` folder, organized by `/ticker/year/quarter/`
- for a given report, we generate the following files:
    - from `grabbers/sec_document_grabber.py`:
        - `[reportName].html` - the raw document pulled down from the SEC filing.
        - `[reportName].md` - html stripped out into a markdown file
        - `[reportname]_trimmed.md` - a further trimmed markdown file for easier reading
    - from `grabbers/transcript_grabber.py`
        - `[reportname]_meeting_transcript.json` - the transcript of the actual meeting. 