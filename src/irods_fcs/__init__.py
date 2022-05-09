import FlowCal

def load_params(
        filename
        ):
    return FlowCal.io.FCSData(filename).text


def filter_dict(
        dict_in 
        ,keyword_filter = None
        ):
    if keyword_filter is None:
        return dict_in       
    else:
        if not keyword_filter:
            return dict_in
        else:
            dict_out = {}
            for i in keyword_filter:
                if not callable(i):
                    dict_out.update( (k,v) 
                                     for k,v in dict_in.items() if i == k )
                else:
                    dict_out.update( (k,v) 
                                     for k,v in dict_in.items() if i(k) )
            return dict_out

