#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2010 - 2011, University of New Orleans
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
import csv
import sys

"""
 - run this script:
 >> python %s -m MappingFile.txt -o NewMapping.txt
 
 - run check_id_map.py:
 >> macqiime check_id_map.py -m NewMapping.txt -o checkmap -j run_prefix
 
 - check log of check_id_map.py for relevant errors:
 >> grep -v "Removed bad chars" checkmap/NewMapping.log
 
 - take subsets of .fna and .qual as necessary to render them isomorphic
 - run split_libs:
 >> macqiime split_libraries.py -e 0 -m checkmap/NewMapping_corrected.txt -f MySeqs.fna -q MyQual.qual -o splib-out -j run_prefix -b 8
 
""" % sys.argv[0]

if __name__ == "__main__":
    #import pdb;pdb.set_trace()
    sargs = dict(zip(sys.argv[1::2],sys.argv[2::2]))

    mapping = open(sargs["-m"])
    newmapping = open(sargs["-o"],"w")

    dialect = csv.excel_tab()

    mapping_csv = csv.reader(mapping, dialect)
    newmapping_csv = csv.writer(newmapping, dialect)#todo check delims, linebrs

    heads = mapping_csv.next()
    newmapping_csv.writerow(heads[:-1]+["run_prefix"]+heads[-1:])

    for row in mapping_csv:
        newmapping_csv.writerow(row[:-1]+[row[0]]+row[-1:])

    map(file.close,[mapping,newmapping])
    
 
