import scraperwiki
from bs4 import BeautifulSoup
from datetime import datetime

'''
03/30/2012
Scraper for Fed Meeting Logs.

Fed top-level links:
http://www.federalreserve.gov/newsevents/reform_systemic.htm
http://www.federalreserve.gov/newsevents/reform_derivatives.htm
http://www.federalreserve.gov/newsevents/reform_interchange.htm
http://www.federalreserve.gov/newsevents/reform_payments.htm
http://www.federalreserve.gov/newsevents/reform_consumer.htm
http://www.federalreserve.gov/newsevents/reform_resolution.htm
'''

BASE = "http://www.federalreserve.gov"
#Dictionary of Category: url pairs:
FED_MEETINGS = {
    "Systemic Designations, Enhanced Prudential Standards, and Banking Supervision and Regulation": "/newsevents/reform_systemic.htm",
    "Derivatives Markets and Products": "/newsevents/reform_derivatives.htm",
    "Interchange Fees": "/newsevents/reform_interchange.htm",
    "Payments, Settlement and Clearing Activities and Utilities": "/newsevents/reform_payments.htm",
    "Consumer Financial Protection": "/newsevents/reform_consumer.htm",
    "Resolution Framework": "/newsevents/reform_resolution.htm"
}

def main():
    for category, url in FED_MEETINGS.iteritems():
        scrape_page(BASE+url, category)



def scrape_page(url, category):
    '''
    Scrapes a single page of the Fed meeting logs.
    url: the page url
    category: String for the category of all meetings on page.
    '''

    raw_page = scraperwiki.scrape(url)
    page_soup = BeautifulSoup(raw_page)
    table = page_soup.find('table', {"class":"earegulate"})
    
    #Find the table and get the enry for each row.
    all_entries = []
    all_rows = table.find_all("tr")

    subcategory = ""

    for row in all_rows:
        new_entry = {}
        cols = row.find_all('td')
        if len(cols) != 3: 
            header = row.find('th')
            if "Attachment" not in header.get_text(): subcategory = header.get_text()
            continue
    
        new_entry['category'] = category
        new_entry['subcategory'] = subcategory

        new_entry['fullname'] = cols[0].get_text()
        new_entry['name'] = new_entry['fullname'].replace("(PDF)", "").replace("Meeting", "").strip()
        new_entry['link'] = cols[0].find('a').get('href')
        date_raw = cols[1].get_text().strip()
        try:
            date = datetime.strptime(date_raw, "%m/%d/%Y").date()
        except:
            date = datetime.strptime(date_raw.split('-')[0], "%m/%d/%Y").date()
            print new_entry['name'] + ": " + date_raw
        new_entry['date'] = date
        new_entry['type'] = cols[2].get_text()
    
        #new_entry['key'] = new_entry['name'] + ": " + date_raw
        all_entries.append(new_entry)

    #Update database:
    scraperwiki.sqlite.save(['category', 'name', 'date'], all_entries, table_name="MeetingTable1")

main()import scraperwiki
from bs4 import BeautifulSoup
from datetime import datetime

'''
03/30/2012
Scraper for Fed Meeting Logs.

Fed top-level links:
http://www.federalreserve.gov/newsevents/reform_systemic.htm
http://www.federalreserve.gov/newsevents/reform_derivatives.htm
http://www.federalreserve.gov/newsevents/reform_interchange.htm
http://www.federalreserve.gov/newsevents/reform_payments.htm
http://www.federalreserve.gov/newsevents/reform_consumer.htm
http://www.federalreserve.gov/newsevents/reform_resolution.htm
'''

BASE = "http://www.federalreserve.gov"
#Dictionary of Category: url pairs:
FED_MEETINGS = {
    "Systemic Designations, Enhanced Prudential Standards, and Banking Supervision and Regulation": "/newsevents/reform_systemic.htm",
    "Derivatives Markets and Products": "/newsevents/reform_derivatives.htm",
    "Interchange Fees": "/newsevents/reform_interchange.htm",
    "Payments, Settlement and Clearing Activities and Utilities": "/newsevents/reform_payments.htm",
    "Consumer Financial Protection": "/newsevents/reform_consumer.htm",
    "Resolution Framework": "/newsevents/reform_resolution.htm"
}

def main():
    for category, url in FED_MEETINGS.iteritems():
        scrape_page(BASE+url, category)



def scrape_page(url, category):
    '''
    Scrapes a single page of the Fed meeting logs.
    url: the page url
    category: String for the category of all meetings on page.
    '''

    raw_page = scraperwiki.scrape(url)
    page_soup = BeautifulSoup(raw_page)
    table = page_soup.find('table', {"class":"earegulate"})
    
    #Find the table and get the enry for each row.
    all_entries = []
    all_rows = table.find_all("tr")

    subcategory = ""

    for row in all_rows:
        new_entry = {}
        cols = row.find_all('td')
        if len(cols) != 3: 
            header = row.find('th')
            if "Attachment" not in header.get_text(): subcategory = header.get_text()
            continue
    
        new_entry['category'] = category
        new_entry['subcategory'] = subcategory

        new_entry['fullname'] = cols[0].get_text()
        new_entry['name'] = new_entry['fullname'].replace("(PDF)", "").replace("Meeting", "").strip()
        new_entry['link'] = cols[0].find('a').get('href')
        date_raw = cols[1].get_text().strip()
        try:
            date = datetime.strptime(date_raw, "%m/%d/%Y").date()
        except:
            date = datetime.strptime(date_raw.split('-')[0], "%m/%d/%Y").date()
            print new_entry['name'] + ": " + date_raw
        new_entry['date'] = date
        new_entry['type'] = cols[2].get_text()
    
        #new_entry['key'] = new_entry['name'] + ": " + date_raw
        all_entries.append(new_entry)

    #Update database:
    scraperwiki.sqlite.save(['category', 'name', 'date'], all_entries, table_name="MeetingTable1")

main()