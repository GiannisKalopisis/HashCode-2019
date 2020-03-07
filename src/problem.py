# import numpy as np

class Problem:

    def __init__(self, inputPath, outputPath):
        # initialising data
        self.readFile(inputPath)

        # initialising results
        self.resData = []
        self.outputPath = outputPath

    # At the end should call writeFile()
    def resolve(self):
        print "NOT IMPLEMENTED"

    def readFile(self, nameFile):
        fl = open(nameFile, "r")

        readLines = fl.readlines()
        firstLine = [int(s) for s in readLines[0].split(' ')]
        self.rows = firstLine[0]
        self.cols = firstLine[1]
        self.dataA = firstLine[2]
        self.dataB = firstLine[3]

        retArray = list()
        for ln in readLines[1:]:
            # retArray.append(map(int, ln.split(' ')))  #Python2.7
            retArray.append([int(s) for s in ln.split(' ')])  # Python 3.6

        self.data = retArray

    def writeFile(self):
        with open(self.outputPath, 'w+') as fl:
            fl.write(str(self.resDataA) + " ")
            fl.write(str(self.resDataB) + "\n")

            for i in range(0, len(self.resData)):
                for j in range(0, len(self.resData[i])):
                    fl.write(str(self.resData[i][j]))
                    if (j != len(self.resData[i]) - 1):
                        fl.write(" ")
                if (i != len(self.resData) - 1):
                    fl.write("\n")
                    
    def getNextSlide(self):
        if len(horPics)==0:
            return 1
        lastSlide = self.resData[-1]
        lastTags = lastSlide[2]
        if lastSlide[1]==1:
            preLastTags = self.resData[self.len(resData)-2][2]
            lastTags = lastTags + list(set(preLastTags) - set(lastTags))
        maxEvalH = 0
        bestPicH = 0
        maxEvalV = 0
        bestPicV = (0,1)
        Score = 0
        evaluation = 0
        i = 0
        tempTags = []
        for i in range(0,len(self.horPics)):
            evaluation = score(lastTags,self.horPics[i][2])*(len(self.horPics)-1) + self.horPics[i][3]
            if (evaluation>maxEvalH):
                maxEvalH = evaluation
                bestPicH = i
                
        for i in range(0,len(self.verPics)):
            for j in range(0,len(self.verPics)):
                if (i==j):
                    continue
                tempTags = self.verPics[i][2] + list(set(self.verPics[j][2]) - set(self.verPics[i][2]))
                evaluation = score(lastTags,tempTags)*(len(self.verPics)/2) + self.verPics[i][3] + self.verPics[j][3]
                if (evaluation>maxEvalV):
                    maxEvalV = evaluation
                    bestPicV = (i,j)
        
        if (maxEvalH > maxEvalV):
            picId = self.horPics[bestPicH][0]
            resData.append(self.horPics[bestPicH])
            del self.horPics[bestPicH]
            for pic in self.horPics:
                pic[3] = pic[3] - score(picId,pic[0])
            
            if maxEvalH==0:
                return 1
            else:
                return 0
        else:
            picIds = self.horPics[bestPicV[0]][0],self.horPics[bestPicV[1]][0]
            resData.append(self.horPics[bestPicH])
            del self.horPics[bestPicH]
            for pic in self.horPics:
                pic[3] = pic[3] - score(picId,pic[0])
            
            if maxEvalH==0:
                return 1
            else:
                return 0

    def writeSolution(self):
        self.addStartingPhoto()
        end = self.addNextSlide()
        counter = 0
        while (end==0):
            end = self.addNextSlide()
            counter = counter + 1


# Problem class initialisation
probExample = Problem("../input/a_example.txt", "../output/outputExample.txt")
# probSmall= Problem("../inputSmall.txt", "../outputSmall.txt")
# probMed = Problem("../inputMedium.txt", "../outputMedium.txt")
# probBig = Problem("../inputBig.txt", "../outputBig.txt")

# Problem resolve
probExample.resolve()
# probSmall.resolve()
# probMed.resolve()
# probBig.resolve()

# Testing output
probExample.writeFile()
