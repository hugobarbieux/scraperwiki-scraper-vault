###################################################################################
# Twitter scraper - designed to be forked and used for more interesting things
###################################################################################

import scraperwiki
import simplejson
import urllib2

# Change QUERY to your search term of choice.
# Examples: 'newsnight', 'from:bbcnewsnight', 'to:bbcnewsnight'
QUERY = 'jc penny'
RESULTS_PER_PAGE = '100'
RESULT_TYPE = 'recent'
NUM_PAGES = 50
ENTITIES = 'true'


for page in range(1, NUM_PAGES+1):
    base_url = 'http://search.twitter.com/search.json?q=%s&rpp=%s&page=%s&result_type=%s&include_entities=%s' \
         % (urllib2.quote(QUERY), RESULTS_PER_PAGE, page, RESULT_TYPE, ENTITIES)
    try:
        results_json = simplejson.loads(scraperwiki.scrape(base_url))
        for result in results_json['results']:
            #print result
            data = {}
            data['id'] = result['id']
            data['text'] = result['text']
            data['from_user'] = result['from_user']
            data['created_at'] = result['created_at']
            data['geo'] = result['geo']
            data['entities'] = result['entities']
            print data['from_user'], data['text'], data['geo'], data['entities']
            scraperwiki.sqlite.save(["id"], data)
    except:
        print 'Oh dear, failed to scrape %s' % base_url
        break
    

###################################################################################
# Twitter scraper - designed to be forked and used for more interesting things
###################################################################################

import scraperwiki
import simplejson
import urllib2

# Change QUERY to your search term of choice.
# Examples: 'newsnight', 'from:bbcnewsnight', 'to:bbcnewsnight'
QUERY = 'jc penny'
RESULTS_PER_PAGE = '100'
RESULT_TYPE = 'recent'
NUM_PAGES = 50
ENTITIES = 'true'


for page in range(1, NUM_PAGES+1):
    base_url = 'http://search.twitter.com/search.json?q=%s&rpp=%s&page=%s&result_type=%s&include_entities=%s' \
         % (urllib2.quote(QUERY), RESULTS_PER_PAGE, page, RESULT_TYPE, ENTITIES)
    try:
        results_json = simplejson.loads(scraperwiki.scrape(base_url))
        for result in results_json['results']:
            #print result
            data = {}
            data['id'] = result['id']
            data['text'] = result['text']
            data['from_user'] = result['from_user']
            data['created_at'] = result['created_at']
            data['geo'] = result['geo']
            data['entities'] = result['entities']
            print data['from_user'], data['text'], data['geo'], data['entities']
            scraperwiki.sqlite.save(["id"], data)
    except:
        print 'Oh dear, failed to scrape %s' % base_url
        break
    

