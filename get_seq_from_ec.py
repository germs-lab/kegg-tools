#!/usr/bin/python

#this script extract seqeunces in fasta format of EC number
#usage: python get_seq_from_ec.py ecnumber path_to_kegg > seq.fasta
#example: python get_seq_from_ec.py 3.2.1.4 ./kegg > ec.3.2.1.4.fasta

import sys
import gzip
import os
import glob

def read_gene(path,org,gene_list):
    org_file = path+"/genes/organisms/"+org+"/*.nuc*"
    list =  gene_list[org]
    
    for filename in glob.glob(org_file):
        if filename[-2:] == 'gz':
            gb_file = gzip.open(filename,'rb')
        else:
            gb_file = open(filename,'r')
        flag = 0
        for line in gb_file:
            if line[:1] == ">":
                flag = 0
                for gene in list:
                    if gene in line:
                        print line,
                        flag = 1
            elif flag == 1:
                print line,
        gb_file.close()

def read_gene_list(ko, ko_file):
    gene_list = {}
    ko_list = open(ko_file, 'r')
    for line in ko_list:
        spl = line.strip().split('\t')
        if spl[0][3:] == ko:
            gene =  spl[1].split(':')
            if gene_list.has_key(gene[0]):
                temp = gene_list[gene[0]]
                temp.append(gene[1])
                gene_list[gene[0]] = temp
            else:
                gene_list[gene[0]] = [gene[1]]
    ko_list.close()
    return gene_list

def read_ec_list(ec_file):
    ec = open(ec_file,'r')
    ec_list = {}
    for line in ec:
        spl = line.strip().split('\t')
        if ec_list.has_key(spl[1][3:]):
            temp = ec_list[spl[1][3:]]
            temp.append(spl[0][3:])
            ec_list[spl[1][3:]] = temp
        else:
            ec_list[spl[1][3:]] = [spl[0][3:]]
    ec.close()
    return ec_list

def main():
    #read ec
    path = sys.argv[2]
    ec_file = path+"/genes/ko/ko_enzyme.list"
    ec_list = read_ec_list(ec_file)
    ko_file = path+"/genes/ko/ko_genes.list"
    for ko in ec_list[sys.argv[1]]:
        #read ko
        gene_list = read_gene_list(ko, ko_file)
        #read gene
        for item in gene_list.items():
            org = item[0]
            read_gene(path,org,gene_list)

if __name__ == "__main__":
    main()
