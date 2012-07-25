"""Executor for http get request,
set option url with * asterisk sign to give
hints"""

import urllib2

LIST_OPTIONS = ['url', 'cookie', 'user_agent']


def execute(options, payloads, logging):
    url = options.get('url')
    cookie = options.get('cookie')
    user_agent = options.get('user_agent')

    #check if there is asterisk
    if url.find('*') == -1:
        print "you must specify * in your url"
        return

    print "run httpget for url %s" % url
    logging.info("run httpget for url %s" % url)

    for payload in payloads:
        current_url = url.replace('*', payload)
        print "current url: %s" % current_url
        logging.info("current url: %s" % current_url)
        try:
            request = urllib2.Request(current_url)
            request.add_header(
                    'Cookie',
                    cookie)
            request.add_header(
                    'User-agent',
                    user_agent)
            response = urllib2.urlopen(request, timeout=10)
        except urllib2.HTTPError as e:
            print e
            logging.info(e)
            continue
        except Exception as e:
            print e
            logging.info(e)
            continue
        print response.code
        logging.info(response.code)
