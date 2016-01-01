from FileUtils import *

"""
Transcribing DNA into RNA

http://rosalind.info/problems/rna/
"""

def dnaToRNA(s):
    rna = ""

    for base in s:
        if base == "T":
            rna += "U"
        else:
            rna += base

    return rna

contents = FileUtils.readFile(FileUtils.DATA_FILES_DIR + "rosalind_rna.txt")
print dnaToRNA(contents)