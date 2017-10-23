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


    result = [""]
    for key, value in all_gene.items():
        result.append(key)
    print '\t'.join(result)

    for sample, value in count.items():
        result = [sample]
        for gene in all_gene.items():
            if value.has_key(gene[0]):
                result.append(value[gene[0]])
            else:
                result.append("0")
        print '\t'.join(result)



if __name__ == '__main__':
    main()
