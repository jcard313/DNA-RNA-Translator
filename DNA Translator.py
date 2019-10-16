
sequence = input("Please input your DNA sequence: ").lower().strip().strip()
sequenceList = list(sequence)


def DNATranslator(sequenceList):
    for basePair in range(len(sequenceList)):
        if sequenceList[basePair] == "a":
            sequenceList[basePair] = "t"
        elif sequenceList[basePair] == "t":
            sequenceList[basePair] = "a"
        elif sequenceList[basePair] == "g":
            sequenceList[basePair] = "c"
        elif sequenceList[basePair] == "c":
            sequenceList[basePair] = "g"

DNATranslator(sequenceList)
sequence = "".join(sequenceList).upper()
print(sequence)
