"""Executor for http get request,
set option url with * asteric sign to give
hints"""

import urllib2

LIST_OPTIONS = ['url']


def execute(options, payloads):
    url = options.get('url')
    #check if there is asteric
    if url.find('*') == -1:
        print "you must specify * in your url"
        return

    print "run httpget for url %s" % url
    for payload in payloads:
        current_url = url.replace('*', payload)
        print "current url: %s" % current_url
        try:
            response = urllib2.urlopen(current_url)
        except urllib2.HTTPError as e:
            print e
            continue
        except Exception as e:
            print e
            continue
        print response
