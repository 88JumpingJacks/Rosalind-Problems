from FileUtils import *

"""
Counting Point Mutations

http://rosalind.info/problems/hamm/
"""

def getHammingDistance(s, t):
    if len(s) != len(t):
        raise Exception("Input strings must have equal length")

    hammingDistance = 0

    for index in range(len(s)):
        if s[index] != t[index]:
            hammingDistance += 1

    return hammingDistance

content = FileUtils.readFile(FileUtils.DATA_FILES_DIR + "rosalind_hamm.txt")
content = content.splitlines()

print getHammingDistance(content[0], content[1])
