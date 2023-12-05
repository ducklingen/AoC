from math import ceil

inputString = (
    "59764635797473718052486376718142408346357676818478503599633670059885748195966091103097769012608550645686932996546030476521264521211192035231303791868456877717957482002303790897587593845163033589025995509264282936119874431944634114034231860653524971772670684133884675724918425789232716494769777580613065860450960426147822968107966020797566015799032373298777368974345143861776639554900206816815180398947497976797052359051851907518938864559670396616664893641990595511306542705720282494028966984911349389079744726360038030937356245125498836945495984280140199805250151145858084911362487953389949062108285035318964376799823425466027816115616249496434133896"
    * 10000
)

offset = int(inputString[0:7])

input = list(inputString)


def completePhase(input):
    nextPhase = ""

    dimension = len(input)

    for i in range(dimension):
        # pattern = ("0"*(i) + "1"*(i+1) + "0"*(i+1) + "-1"*(i+1)+ "0")*5
        pattern = (
            [0] * i + [1] * (i + 1) + [0] * (i + 1) + [-1] * (i + 1) + [0]
        ) * (ceil(dimension / (4 * (i + 1))))

        outputDigit = 0

        for j in range(dimension):
            # print(input[j] + " * " + str(pattern[j]))
            outputDigit += int(input[j]) * pattern[j]
            # print(outputDigit)

        print(outputDigit)
        nextPhase += str(abs(outputDigit) % 10)

    return nextPhase


for i in range(100):
    input = completePhase(input)
    print(input)
