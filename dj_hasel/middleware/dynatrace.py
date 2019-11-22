import oneagent

class DynatraceMonkeyPatch(object):

    def __init__(self):

        self.init_result = oneagent.initialize()

    def process_request(self, request):

        # print '>'*79
        # print dir(request)
        # print request.session.session_key,'sd'

        with oneagent.get_sdk().trace_incoming_remote_call('method', 'service', 'endpoint'):
            pass

        return None