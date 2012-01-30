#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2010 - 2011, University of New Orleans
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#

import sys

sep = '_'

def seqs(f, include_comments = False):
    """A generator for the sequences in a FASTA file"""
    seq = ""
    f = f if include_comments else (l for l in f if not l.startswith(";"))
    for line in f:
        if seq != "" and line.startswith('>'):
            yield seq
            seq = ""
        seq += line
    if seq != "":
        yield seq

samples = set()

for seq in seqs(open(sys.argv[1])):
    head = seq.split()[0]
    sample_id = head.strip('>').split(sep)[0]
    samples.add(sample_id.strip('MZH-').strip('A').strip())#temporary. get rid of strip()s

for s in samples:
    print s
