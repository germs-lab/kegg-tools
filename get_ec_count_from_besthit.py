#!/usr/bin/python

"""
"""

import sys

def main():
    #read
    enzyme_file = sys.argv[1]
    gene_file = sys.argv[2]
    besthit_file = sys.argv[3]

    ec = {}
    for line in open(enzyme_file,'r'):
        spl = line.strip().split('\t')
        ec[spl[0]] = spl[1]

    gene = {}
    for line in open(gene_file,'r'):
        spl = line.strip().split('\t')
        gene[spl[1]] = spl[0]

    count = {}
    for line in open(besthit_file,'r'):
        spl = line.strip().split('\t')
        if gene.has_key(spl[1]):
            ko = gene[spl[1]]
            if ec.has_key(ko):
                ec_num = ec[ko]
                if count.has_key(ec_num):
                    count[ec_num] += 1
                else:
                    count[ec_num] = 1

    for key,value in count.items():
        print besthit_file + '\t' + key + '\t' + str(value)


if __name__ == '__main__':
    main()


