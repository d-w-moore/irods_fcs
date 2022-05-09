# irods-fcs

As of version 0.0.1, this Python3 module contains the basic functionality to

  - pull keyword/value parameter pairs from the headers of FCS files

  - if the file is registered in iRODS, filter the parameter pairs 
     optionally via a list of desired keywords and translate the
     selected parameters into metadata tags that will annotate the
     corresponding iRODS data object.

