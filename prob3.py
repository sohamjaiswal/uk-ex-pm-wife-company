def getAscendingSubsequences(entries):
    subsequences, sequence = [], []
    for entry in entries:
        if (not sequence) or (entry >= sequence[-1]):
            sequence.append(entry)
        else:
            subsequences.append(sequence)
            sequence = [entry]
    subsequences.append(sequence)
    return subsequences
def doesObeyLogic(sequence):
    obeys = True
    if len(sequence) == 1:
        return False
    for i in range(0, len(sequence)-1):
        if not ((sequence[i] & sequence[i+1])*2<(sequence[i] | sequence[i+1])):
            obeys = False
            break
    return obeys
def getLongestWithLogic(subsequences):
    longest = []
    for sequence in subsequences:
        if (len(sequence) > len(longest)) and doesObeyLogic(sequence):
            longest = sequence
    return longest
numEntries = int(input("Enter the number of entries: "))
entries = []
for i in range(0, numEntries):
    entry = int(input("Enter entry " + str(i + 1) + ": "))
    entries.append(entry)
print(len(getLongestWithLogic(getAscendingSubsequences(entries))))