"""http post executor, using requests.
Set fields with comma separated values"""
import requests


LIST_OPTIONS = ['url', 'fields']


def execute(options, payloads, logging):
    url = options.get('url')
    fields = options.get('fields')
    fields = fields.split(',')
    data = {}
    for payload in payloads:
        for field in fields:
            data[field] = payload
        logging.info('payload: %s' % payload)
        logging.info(data)
        r = requests.post(url, data=data, verify=False,
                allow_redirects=False)
        logging.info('status code: %s' % r.status_code)
        logging.info('response: %s' % r.text)
