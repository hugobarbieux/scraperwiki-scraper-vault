import scraperwiki
import urllib2
import lxml.etree

url = "http://www.p12.nysed.gov/irs/pmf/2011-12/2012-Stat-15.pdf"
pdfdata = urllib2.urlopen(url).read()
print "The pdf file has %d bytes" % len(pdfdata)
xmldata = scraperwiki.pdftoxml(pdfdata)
print "After converting to xml it has %d bytes" % len(xmldata)

root = lxml.etree.fromstring(xmldata)

# this line uses xpath to find <text tags
lines = root.findall('.//text')
record = {}
datacount = 0
group = "0"

for line in lines:
    fontvalue = line.get("font")
    linetop = line.get("top")
    #print fontvalue, linetop, line.text
    if fontvalue == "3" and group=="1":
        datacount = 0
        #print record
        scraperwiki.sqlite.save(['bedscode'], record)
        record = {}
        record["district"] = line.text
    if fontvalue == "3"and group=="0":
        group = "1"
        record["district"] = line.text
    elif fontvalue == "4":
        record["bedscode"] = line.find('.//b').text
    elif fontvalue == "5":
        datacount = datacount +1
        record["Data"+str(datacount)] = line.text
    else:
        print "ignore"

import scraperwiki
import urllib2
import lxml.etree

url = "http://www.p12.nysed.gov/irs/pmf/2011-12/2012-Stat-15.pdf"
pdfdata = urllib2.urlopen(url).read()
print "The pdf file has %d bytes" % len(pdfdata)
xmldata = scraperwiki.pdftoxml(pdfdata)
print "After converting to xml it has %d bytes" % len(xmldata)

root = lxml.etree.fromstring(xmldata)

# this line uses xpath to find <text tags
lines = root.findall('.//text')
record = {}
datacount = 0
group = "0"

for line in lines:
    fontvalue = line.get("font")
    linetop = line.get("top")
    #print fontvalue, linetop, line.text
    if fontvalue == "3" and group=="1":
        datacount = 0
        #print record
        scraperwiki.sqlite.save(['bedscode'], record)
        record = {}
        record["district"] = line.text
    if fontvalue == "3"and group=="0":
        group = "1"
        record["district"] = line.text
    elif fontvalue == "4":
        record["bedscode"] = line.find('.//b').text
    elif fontvalue == "5":
        datacount = datacount +1
        record["Data"+str(datacount)] = line.text
    else:
        print "ignore"

