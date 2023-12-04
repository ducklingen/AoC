sequence = '3113322113'

def splitSequence(seq):
    list = []
    char = ''
    charSplit = ''

    for i in seq:
        if i == char:
            charSplit += i
        else:
            if not charSplit == '':
                list.append(charSplit)
            charSplit = i
            char = i

    list.append(charSplit)

    return list


for i in range(50):
    splits = splitSequence(sequence)
    sequence = list_to_string([str(len(s))+s[0] for s in splits])
    print(str(i+1) + ": " + sequence)
    print(str(i+1) + ": " + str(len(sequence)))
