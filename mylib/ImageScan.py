import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

class ImageScan():
    IgnoreExt = []
    IgnoreFile = ['.DS_Store']
    DirLimit = 100
    nowdir = 0
    filename = []

    def fnameArrayBuild(self, dirpass):
        self.nowdir += 1
        if self.nowdir >= self.DirLimit:
            return "limitOut"

        dirname = []
        allelemet = os.listdir(dirpass)
        if len(allelemet) == 0:
            return

        for element in allelemet:
            if self.isIgnoreFile(element):
                continue
            
            elementpath = os.path.join(dirpass, element)
            if os.path.isfile(elementpath):
                self.filename.append(elementpath)
            else:
                dirname.append(elementpath)

        if len(dirname) == 0:
            return 

        for nextdir in dirname:
            self.fnameArrayBuild(nextdir)
        
        return self.filename

    def ScanImageGrayScale(self, dirpass):
        filenamelist = self.fnameArrayBuild(dirpass)
        dupfilename = []
        histrs = []
        for file in filenamelist:
            img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
            histr = cv2.calcHist([img],[0],None,[256],[0,256])
            histrs.append(histr)
        length = len(histrs)
        for i, histr in enumerate(histrs):
            tempdupfile = []
            if filenamelist[i] in dupfilename:
                continue
            for j in range(length):
                if i == j:
                    continue
                hist_value = cv2.compareHist(histrs[i], histrs[j], cv2.HISTCMP_CORREL)
                if hist_value == 1.0:
                    tempdupfile.append(filenamelist[j])
            if len(tempdupfile) != 0:
                tempdupfile.append(filenamelist[i])
                self.multiAppndinArray(dupfilename, tempdupfile)
            
        
        return dupfilename



    def isIgnoreFile(self,checkfilestr):
        if checkfilestr in self.IgnoreFile:
            return True
        root, ext = os.path.splitext(checkfilestr)
        if ext in self.IgnoreExt:
            return True
        
        return False
    
    def multiAppndinArray(self, array, values):
        for value in values:
            array.append(value)


class RGBValueObject():
    pass
