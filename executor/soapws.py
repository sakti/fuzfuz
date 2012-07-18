import suds


LIST_OPTIONS = ['wsdl', 'method']


def _get_number_sig(methodname, definition):
    for method, signature in definition.ports[0][1]:
        if method == methodname:
            return len(signature)


def execute(options, payloads):
    wsdl = options.get('wsdl')
    method_name = options.get('method')

    client = suds.client.Client(wsdl)
    number_sig = _get_number_sig(method_name, client.sd[0])

    method = getattr(client.service, method_name)

    print 'target function: %s' % method_name

    for payload in payloads:
        print "\nexecute payload: %s" % payload
        print method(*([payload] * number_sig))
