

quick rundown--

Went to finbot, wanted to start from its sources

Discovered the earnings file
  found out it was attached to the DiscountingCashFlows api
    and THEY now report: NO MORE API AFTER JANUARY 15TH!!!!!!!!!

So, fuck 'em

current key--  DiscountingCashFlows api key - limited to 500/hour (not bad for now)

The real trick is that everyone wants a cut for financial data, even when it's public knowledge. 


So, if we wanna stand this up, we have to either: 
pay

or

ai suggested 
https://www.google.com/finance/
https://www.sec.gov/search-filings
or *manually going to a list of websites*, jfc. 



---

Transcripts are paywall locked as far as I can see for the moment. 

---
Manually excavating the SEC archive

SEC site

https://www.sec.gov/Archives/edgar/data/320193/000032019320000062/aapl-20200627.htm

https://www.sec.gov/edgar/search/#/q=AAPL&filter_ciks=0000320193&filter_entityName=Apple%2520Inc.%2520%2520(AAPL)%2520%2520(CIK%25200000320193)&filter_forms=10-Q


alright, let's take a journey-- this is Apple's Q2 filing for 2024
https://www.sec.gov/Archives/edgar/data/320193/000032019324000081/0000320193-24-000081-index.html

and here's the 10-Q document proper:
https://www.sec.gov/Archives/edgar/data/320193/000032019324000081/aapl-20240629.htm


okay, so, starting from the ticker `AAPL`

we look at this json...

https://www.sec.gov/files/company_tickers.json

to get its CIK value-- "Central Index Key"

Apple's is `320193`

to get their submissions, we have to pad left with four 0s to get to 10 digits...

apple's entity page...

https://data.sec.gov/submissions/CIK0000320193.json


from here, we get access to a lot of info, but I dunno what to grab from here to key into an actual filing document...

slot 35 is:
- form: 10-Q
- accession number: 0000320193-24-000081
- filingDate: 2024-08-02
- reportDate: 2024-06-29
- fileNumber: 001-36743
- filmNumber: 241168182
- primaryDocument: aapl-20240629.htm
- primaryDocDescription: 10-Q


okay. Let's strip down our old links and match a bit-- 

this should be that same document. let's look 

and here's the 10-Q document proper:
https://www.sec.gov/Archives/edgar/data/320193/000032019324000081/aapl-20240629.htm

https://www.sec.gov/Archives/edgar/data/{CIK}/{accession}/{document}


EU-FUCKIN'-REKA

quick adjustment to some busted quarter-based concept the ai initially wrote, I reassessed it, and we got it snapped right down. 

Concpt is proven, now I'm just adjusting the messy bits. 



---


we can also get full ass piles of the data, but they aren't SUPER duper useful... I can't pinpoint any actual filings, just a fuckload of json objects like the appl entity object up there. 

https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip -> 1.2 gigs!!

https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip -> 1.3 gigs!!


oh fuck, okay, so they just... give them to you


