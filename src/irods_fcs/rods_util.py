import os
import sys
from irods.test.helpers import (make_session, home_collection)
from irods.meta import (iRODSMeta, AVUOperation)
from irods.data_object import (iRODSDataObject)

from . import (load_keywords, filter_dict)

def session(**opts):
    return make_session(*opts)

def do_atomic_avu_request (session
                      , data_object
                      , dict_in =()):

    kvpairs = dict(dict_in)
    
    avu_ops = []

    if not isinstance( data_object, iRODSDataObject ):
        data_object = session.data_objects.get( data_object )

    for k,v in dict_in.items():
        avu_ops.append(AVUOperation(operation='add', avu=iRODSMeta(k, v)))

    data_object.metadata.apply_atomic_operations(*avu_ops)

    1;
    
def metadata_demo(fcs_file_name,
                  fcs_data_name = '',
                  keyword_filter = None
        ):

    session = make_session()
    
    # __ Register the FCS file as an iRODS data object. __

    if not fcs_data_name:
        fcs_data_name = home_collection(session) + "/" + os.path.basename(fcs_file_name)
    session.data_objects.register( fcs_file_name, fcs_data_name )

    # __ Load full keyword set from FCS header. __

    all_kw = load_keywords(fcs_file_name)

    # __ Select keyword subset and attach as iRODS metadata. __

    keywords = filter_dict( all_kw,
                            keyword_filter = keyword_filter
                                             )
    do_atomic_avu_request( session,
                           fcs_data_name,
                           keywords )
