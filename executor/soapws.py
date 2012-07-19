"""Executor for soap-based webservice,
all executor must implement ALL_OPTIONS and
execute function"""
import suds


LIST_OPTIONS = ['wsdl', 'method']


def _get_number_sig(methodname, definition):
    "get number of function parameters"
    for method, signature in definition.ports[0][1]:
        if method == methodname:
            return len(signature)


def execute(options, payloads):
    wsdl = options.get('wsdl')
    method_name = options.get('method')

    try:
        client = suds.client.Client(wsdl)
        number_sig = _get_number_sig(method_name, client.sd[0])
        method = getattr(client.service, method_name)
    except Exception as e:
        print e
        return

    print 'target function: %s' % method_name

    for payload in payloads:
        try:
            print "\nexecute payload: %s" % payload
            print method(*([payload] * number_sig))
        except Exception as e:
            print e
