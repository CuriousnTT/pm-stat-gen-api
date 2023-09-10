from pathlib import Path
CURRENTDATASETTYPES = ["xlsx"]

#Probably could get a better name
class FilePathMethods:
    @staticmethod
    def getDataSetPath(dataSetFolderPath : Path, dataSetType : str, dataSetFileName : str):
        fileName = dataSetFileName if dataSetType in dataSetFileName else dataSetFileName.split("." + dataSetType)[0]
        if dataSetType in CURRENTDATASETTYPES:
            return Path.joinpath(dataSetFolderPath, dataSetType, str.format("{fileName}.{dataSetType}", fileName = fileName, dataSetType = dataSetType))
        else:
            return None #TODO change this to return exception later