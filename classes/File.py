import pickle
from classes.DataList import DataList
from os import path


class File(object):

    @staticmethod
    def saveData(data, filePath):
        outfile = open(filePath, 'wb')
        pickle.dump(data, outfile)
        outfile.close()
        return True

    @staticmethod
    def readData(filePath):
        newDict = DataList()
        if path.exists(filePath):
            infile = open(filePath, 'rb')
            newDict = pickle.load(infile)
            infile.close()
        return newDict
