#!/usr/bin/env python3

import pdb, irods_fcs.rods_util
import sys

fcs_file_name = sys.argv[1]
kw_filter = sys.argv[2:]
irods_fcs.rods_util.metadata_demo( fcs_file_name,
                                   keyword_filter = (None if not kw_filter else kw_filter)
                                  )
