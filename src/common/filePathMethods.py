from pathlib import Path

#Broken crap:
"""import sys
curPath = Path.cwd()
if (curPath.name == "pm-stat-gen-api"):
    sys.path.append(str(curPath.joinpath("src","common")))
elif (curPath.name == "src"):
    sys.path.append(str(curPath.joinpath("common")))
elif (curPath.name == "common"):
    sys.path.append(str(curPath))
from common.constants import Constants"""
CURRENTDATASETTYPES = ["xlsx"] #remove and replace with whatever bootleg solution to the import issue we find

#Probably could get a better name
class FilePathMethods:
    @staticmethod
    def getDataSetPath(dataSetFolderPath : Path, dataSetType : str, dataSetFileName : str):
        fileName = dataSetFileName if dataSetType in dataSetFileName else dataSetFileName.split("." + dataSetType)[0]
        print(Path)
        if dataSetType in CURRENTDATASETTYPES:
            return Path.joinpath(dataSetFolderPath, dataSetType, str.format("{fileName}.{dataSetType}", fileName = fileName, dataSetType = dataSetType))
        else:
            return None #TODO change this to return exception later