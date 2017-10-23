#!/usr/bin/python

"""
"""

import sys

def main():
    files = sys.argv[1:]
    all_gene = {}
    count = {}
    for file in files:
        for line in open(file,'r'):
            spl = line.strip().split('\t')
            if not count.has_key(spl[0]):
                count[spl[0]] = {}
            count[spl[0]][spl[1]] = spl[2]
            all_gene[spl[1]] = ""

    print count
    result = [""]
    for key, value in all_gene.items():
        result.append(key)
    print '\t'.join(result)

    for key, value in count.items():
        result = [key]
        for gene in all_gene.items():
            result.append(count[key][gene[0]])
        print '\t'.join(result)



if __name__ == '__main__':
    main()
