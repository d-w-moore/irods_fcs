# irods-fcs

## Summary

As of version 0.0.1, this Python3 module contains the basic functionality to

  - pull keyword/value parameter pairs from the headers of FCS files

  - if the file is registered in iRODS, filter the parameter pairs 
     optionally via a list of desired keywords and translate the
     selected parameters into metadata tags that will annotate the
     corresponding iRODS data object.

These capabilities can be extended to become interoperable with 
   - client side ingest:  https://github.com/irods/irods_capability_automated_ingest
   - data policy via rules implemented in Python: https://github.com/irods/irods_rule_engine_plugin_python

We rely on the PyPI 'FlowCal' module at present

## Setup

On Centos 7 with an iRODS 4.2.11 server installed, we can set up in this way:
```
(as root)  
# sudo apt install python3-tkinter python3-pip python36-virtualenv git
(as irods) 
$ virtualenv-3 ~/py3
$ . ~/py3/bin/activate
(py3) $ git clone http://github.com/d-w-moore/irods_fcs
(py3) $ pip install ./irods_fcs
```

## Demonstration

Using a sample .FCS file:

```
# -- choose a subset of the available keywords in the file header (no filtering if keywords are not entered)

(py3) $ irods_fcs/src/demo.sh /tmp/01-ALL_651149252706-A8.fcs 
enter keywords > SMID TBID

# -- list the registered data object's metadata tags that were attached 

(py3) $ imeta ls -d  `ipwd`//01-ALL_651149252706-A8.fcs
AVUs defined for dataObj /tempZone/home/rods/01-ALL_651149252706-A8.fcs:
attribute: SMID
value: CA012-004_20OCT20_0024 00212_C1D15
units: 
----
attribute: TBID
value: 2e48cac4-566e-4d07-bf90-44fc3e568e12
units: 
```
