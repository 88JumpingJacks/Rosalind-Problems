from FileUtils import *

"""
Complementing a Strand of DNA

http://rosalind.info/problems/revc/
"""

complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def reverseComplementDNA(dna):
    reverseComplement = ""

    for base in dna:
        reverseComplement = complements[base] + reverseComplement

    return reverseComplement

contents = FileUtils.readFile(FileUtils.dataFiles_Dir + "rosalind_revc.txt")

print reverseComplementDNA(contents)