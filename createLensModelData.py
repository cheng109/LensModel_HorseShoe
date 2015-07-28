

class image:
    def __init__(self, (xpos, ypos), flux, sigmaXpos,sigmaYpos, sigmaFlux):
        centerX = 150
        centerY = 150
        pixelScale = 0.04
        self.xpos = (xpos-centerX) * pixelScale
        self.ypos = (ypos-centerY) * pixelScale
        self.flux = flux
        self.sigmaXpos = sigmaXpos
        self.sigmaYpos = sigmaYpos
        self.sigmaFlux = sigmaFlux


    def getImageItem(self):
        return    str(self.xpos)+ "\t" \
                  + str(self.ypos) + "\t"\
                  + str(self.flux) +"\t"\
                  + str(self.sigmaXpos) + "\t"\
                  + str(self.sigmaFlux) + "\t"\
                  + str(0) + "\t"\
                  + str(0) +"\t"


def createLensModelData(imageDict, dataFileName):
    header = """
1
0	0	0.05
0.0	10000.0
0.0	10000.0
0.0	10000.0

"""
    f = open(dataFileName, 'w')
    f.write(header + str(len(imageDict)))

    for key, val in imageDict.items():
        f.write("\n\n" + str(len(val)))
        for i in range(len(val)):
            img = image(val[i], flux=1000, sigmaXpos=0.05, sigmaYpos=0.05, sigmaFlux=1000)
            f.write( "\n" + img.getImageItem())
    f.write("\n")
    f.close()


def main():
    imageDict = {}
    #positions of images: pixel
    imageDict['A'] =  [(63, 264), (277, 183)]
    imageDict['B'] =  [(71,272), (266, 96)]
    imageDict['C'] =  [(93,282), (112, 46)]

    dataFileName = "horseshoe.data"
    createLensModelData(imageDict, dataFileName)


if __name__=="__main__":
    main()