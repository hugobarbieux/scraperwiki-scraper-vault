import scraperwiki
import urllib
import lxml.etree, lxml.html
import re

pdfurl = "http://www.merck.com/corporate-responsibility/docs/business-ethics-transparency/3Q09-Transparency-Report.pdf"


# (harder example to work on: http://www.nihe.gov.uk/schemes_accepted_010109_to_310309.pdf )
pdfdata = urllib.urlopen(pdfurl).read()
pdfxml = scraperwiki.pdftoxml(pdfdata)
root = lxml.etree.fromstring(pdfxml)

for page in root:
    assert page.tag == 'page'
    #print "page details", page.attrib
    pagelines = { }
    for v in page:
        if v.tag == 'text':
            text = re.match('(?s)<text.*?>(.*?)</text>', lxml.etree.tostring(v)).group(1)   # there has to be a better way here to get the contents
            top = int(v.attrib.get('top'))
            if top not in pagelines:
                pagelines[top] = [ ]
            pagelines[top].append((int(v.attrib.get('left')), text))
    lpagelines = pagelines.items()
    lpagelines.sort()
    for top, line in lpagelines:
        line.sort()
        key = page.attrib.get('number') + ':' + str(top)
        #print top, line
        scraperwiki.datastore.save(unique_keys=[ 'key' ], data={ 'key' : key, 'line' : line })
import scraperwiki
import urllib
import lxml.etree, lxml.html
import re

pdfurl = "http://www.merck.com/corporate-responsibility/docs/business-ethics-transparency/3Q09-Transparency-Report.pdf"


# (harder example to work on: http://www.nihe.gov.uk/schemes_accepted_010109_to_310309.pdf )
pdfdata = urllib.urlopen(pdfurl).read()
pdfxml = scraperwiki.pdftoxml(pdfdata)
root = lxml.etree.fromstring(pdfxml)

for page in root:
    assert page.tag == 'page'
    #print "page details", page.attrib
    pagelines = { }
    for v in page:
        if v.tag == 'text':
            text = re.match('(?s)<text.*?>(.*?)</text>', lxml.etree.tostring(v)).group(1)   # there has to be a better way here to get the contents
            top = int(v.attrib.get('top'))
            if top not in pagelines:
                pagelines[top] = [ ]
            pagelines[top].append((int(v.attrib.get('left')), text))
    lpagelines = pagelines.items()
    lpagelines.sort()
    for top, line in lpagelines:
        line.sort()
        key = page.attrib.get('number') + ':' + str(top)
        #print top, line
        scraperwiki.datastore.save(unique_keys=[ 'key' ], data={ 'key' : key, 'line' : line })
