def getAscendingSubsequences(entries):
    subsequences, sequence = [], []
    for entry in entries:
        if not sequence or entry > sequence[-1]:
            sequence.append(entry)
        else:
            subsequences.append(sequence)
            sequence = [entry]
    subsequences.append(sequence)
    return subsequences
def doesObeyLogic(sequence):
    return all((sequence[i] & sequence[i+1])*2 < (sequence[i] | sequence[i+1]) for i in range(len(sequence)-1))
def getLongestWithLogic(subsequences):
    return max((sequence for sequence in subsequences if doesObeyLogic(sequence)), key=len, default=[])
numEntries = int(input("Enter the number of entries: "))
entries = [int(input(f"Enter entry {i + 1}: ")) for i in range(numEntries)]
print(len(getLongestWithLogic(getAscendingSubsequences(entries))))