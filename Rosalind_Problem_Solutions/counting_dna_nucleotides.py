from FileUtils import *

"""
Counting DNA Nucleotides

http://rosalind.info/problems/dna/
"""

def countNucleotides(s):
    # Dictionary to keep track of occurrences of each nucleotide
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for base in s.strip():
        count[base] += 1

    return count


# todo read input file
file = open(FileUtils.DATA_FILES_DIR + "rosalind_dna.txt", "r")

# Initialize dictionary storing counts for each nucleotide
count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

with file as f:
    for line in f:
        temp = countNucleotides(line)
        count['A'] += temp['A']
        count['C'] += temp['C']
        count['G'] += temp['G']
        count['T'] += temp['T']

print count['A'], count['C'], count['G'], count['T']

file.close()
