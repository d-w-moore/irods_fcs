import FlowCal

import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

FCS_VALUE_MAX_LEN = 2700


def load_keywords( filename
        ):
    return FlowCal.io.FCSData(filename).text


def filter_dict(
        dict_in 
        ,keyword_filter = None
        ):
    if keyword_filter is None:
        dict_out = dict_in
    else:
        dict_out = {}
        for i in keyword_filter:
            if not callable(i):
                dict_out.update( (k,v) 
                                 for k,v in dict_in.items() if i == k )
            else:
                dict_out.update( (k,v) 
                                 for k,v in dict_in.items() if i(k) )

    keys = list(dict_out.keys())
    for k in keys:
        v = dict_out[k].encode('utf8')
        if len(v) > FCS_VALUE_MAX_LEN:
            logger.warning( "Skipping FCS '%s' keyword since the value exceeds %d bytes", k, FCS_VALUE_MAX_LEN )
            del dict_out[k]

    return dict_out
