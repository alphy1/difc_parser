# DIFC Parser

### Author: Alfiya Mussabekova

## Description
This project is the parser for https://www.difc.ae/public-register/, which extract information about companies using `scrapy` and saves the data for future analysis.
Example of extracted data:
``` 
{'Business activities': 'Holding Company',
 'Commercial License Validity Date': '21 09 2022',
 'Data Protection Officer Appointed': 'No',
 'Date of Incorporation': '22 09 2021',
 'Directors': 'Karim Mohamad Farouk Solh',
 'Legal Structure': 'Private Company',
 'Name': 'GC Equity Co-Invest IV Holding Limited',
 'Personal Data Processing Operations': 'No',
 'Processing of Special Categories of Personal Data': 'No',
 'Registered Number': 5060,
 'Registered offices': 'Unit Unit 01, Level 30, Currency Tower 2, Dubai '
                       'International Financial Centre, Dubai, , United Arab '
                       'Emirates',
 'Share Capital': '100 issued shares of Class class A with a nominal value of '
                  'USD 1 per Share',
 'Shareholders': 'Gulf Capital PJSC',
 'Status of Registration': 'Active',
 'Trading Name': 'GC Equity Co-Invest IV Holding Limited',
 'Transfer of Personal Data from the DIFC': 'No',
 'Type of License': 'Non Regulated'}
```
## Prerequisites
``` 
Python 3.8
docker
docker-compose
```

## How to run
1. Create virtual environment:
```
make venv
```
2. Run `mongodb` in container:
``` 
make db
```
3. Scrape website to parse information about companies and save it in `mongodb`:
``` 
make run
```
4. To specify number of companies to parse:
``` 
scrapy crawl difc -a companies=<number>
```
Also, you can specify pages to crawl, each page contains 10 companies:
``` 
scrapy crawl difc -a pages=10
```
By default ```scrapy crawl difc``` will parse 2 pages or 20 companies.

5. Run tests:
```
make test
```
