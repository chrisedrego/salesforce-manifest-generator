import json

@staticmethod
def loadConfig(filePathName):
    with open(filePathName,'r')  as fp:
        return json.load(fp)