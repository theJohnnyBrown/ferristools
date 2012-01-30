#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2010 - 2011, University of New Orleans
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
from cogent.parse.fasta import MinimalFastaParser
import sys

def usage():
    print """USAGE: %s <fastafile> namestems
    Where namestems is a list in quotes, with entries separated by commas, e.g.
        "JN031811-1, JN031811-2, Jn031811-3"

    or %s <fastafile> -f stemsfile
    Where stemsfile is a the path to a file containing one list entry per line

    any sequences in the fasta file whose names begin with one of the entries in the list will be printed
    """ % sys.argv[0]
    sys.exit(-1)

if __name__ == "__main__":
    l = len(sys.argv)
    if l not in [3,4] or sys.argv[1] == "-h":
        usage()
    else:
        fna = MinimalFastaParser(open(sys.argv[1]))
        if l == 3:
            stems = [e.strip() for e in sys.argv[2].split(",")]
        elif sys.argv[2] == '-f':
            try:
                stems = [e.strip() for e in open(sys.argv[3]).read().split("\n")]
            except IOError:
                usage()
        else:
            usage()
    for seq in iter(fna):
        for stem in stems:
            if seq[0].startswith(stem):
                print ">%s\n%s" % (seq)#print inserts a trailing newline
                break
            
