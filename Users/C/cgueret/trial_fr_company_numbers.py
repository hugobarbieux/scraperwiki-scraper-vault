import urllib2
import scraperwiki
from BeautifulSoup import BeautifulSoup

CODE_APE = "1011Z"
DEPT = "37"
FORM_URL = "http://www.societe.com/cgi-bin/liste"

# Keys for mapping text fields in the page to column names in the table
KEYS = { 
    'Nom commercial' : 'CompanyName',
    'SIRET' : 'CompanyNumber',
    'RCS' : 'RCS',
    'Forme juridique' : 'EntityType'
}


# Get the list of all the companies
debut = 1
stop = False
societees = []
while not stop:
    url = "http://www.societe.com/cgi-bin/liste?ape=%s&dep=%s&debut=%d" % (CODE_APE, DEPT, debut)
    document = BeautifulSoup(urllib2.urlopen(url).read())
    document_nok = document.findAll(text="Erreur de formulaire")
    if document_nok:
        stop = True
    links = document.findAll('a', attrs={'class':'blk2'})
    for link in links:
        societees.append({'name':link.getText(), 'page':link.get('href')})
    debut = debut + 10
    del document
print "Found %d companies" % len(societees)


# Download the information about companies, one by one
for societe in societees:
    record = {}
    record['CompanyName'] = societe['name']
    url = "http://www.societe.com%s" % societe['page']
    document = BeautifulSoup(urllib2.urlopen(url).read())
    trs = document.findAll('tr',attrs={'align':'left'})
    for tr in trs:
        tds = tr.findAll('td')
        if len(tds) == 2:
            text = tds[0].getText()
            value = tds[1].getText()
            print '--%s--' % text
            if text in KEYS.keys():
                record[KEYS[text]] = value
    scraperwiki.datastore.save(["CompanyNumber"], record)

import urllib2
import scraperwiki
from BeautifulSoup import BeautifulSoup

CODE_APE = "1011Z"
DEPT = "37"
FORM_URL = "http://www.societe.com/cgi-bin/liste"

# Keys for mapping text fields in the page to column names in the table
KEYS = { 
    'Nom commercial' : 'CompanyName',
    'SIRET' : 'CompanyNumber',
    'RCS' : 'RCS',
    'Forme juridique' : 'EntityType'
}


# Get the list of all the companies
debut = 1
stop = False
societees = []
while not stop:
    url = "http://www.societe.com/cgi-bin/liste?ape=%s&dep=%s&debut=%d" % (CODE_APE, DEPT, debut)
    document = BeautifulSoup(urllib2.urlopen(url).read())
    document_nok = document.findAll(text="Erreur de formulaire")
    if document_nok:
        stop = True
    links = document.findAll('a', attrs={'class':'blk2'})
    for link in links:
        societees.append({'name':link.getText(), 'page':link.get('href')})
    debut = debut + 10
    del document
print "Found %d companies" % len(societees)


# Download the information about companies, one by one
for societe in societees:
    record = {}
    record['CompanyName'] = societe['name']
    url = "http://www.societe.com%s" % societe['page']
    document = BeautifulSoup(urllib2.urlopen(url).read())
    trs = document.findAll('tr',attrs={'align':'left'})
    for tr in trs:
        tds = tr.findAll('td')
        if len(tds) == 2:
            text = tds[0].getText()
            value = tds[1].getText()
            print '--%s--' % text
            if text in KEYS.keys():
                record[KEYS[text]] = value
    scraperwiki.datastore.save(["CompanyNumber"], record)

