import pandas as pd
import sys
from pathlib import Path

curPath = Path.cwd()
if (curPath.name == "pm-stat-gen-api"):
    sys.path.append(str(curPath))
elif (curPath.name == "src"):
    sys.path.append(str(curPath.parent))
elif (curPath.name == "stadiumConverter"):
    sys.path.append(str(curPath.parent.parent))
import src.common.filePathMethods as fpm
from src.common.constants import Constants

class PmStadiumConverter():
    def __init__(self, datapathName, rootDirectory):
        self.dataSetPathName = datapathName
        self.rootDirectory = rootDirectory

    def __checkParentForDesiredFolder(self, curDir : Path, desiredFolderName : str, limitFolderName : str):
        for folder in curDir.iterdir():
            if desiredFolderName in folder.name:
                return folder
        if limitFolderName in curDir.name:
            return "Desired folder not found" #TODO change this to return exception later
        self.__checkParentForDesiredFolder(curDir.parent, desiredFolderName, limitFolderName)

    def __filterUnwantedColumns(self, dFrame : dict):
        for column in dFrame.columns:
            if column not in Constants.DESIREDCOLUMNS.value:
                del dFrame[column]

    def __ConverterSeperateDt(self, gameFolderPath : Path, fileExt : str):
        dataFiles = gameFolderPath.glob("*" + fileExt)
        data = {}
        for file in dataFiles:
            dt = pd.read_csv(str(file))
            self.__filterUnwantedColumns(dt)
            data[file.name.split(".")[0]] = dt
        return data

    #can be more efficient by using dask.DataFrame
    def __ConverterAllDt(self, gameFolderPath : Path, fileExt : str):
        dataFiles = gameFolderPath.glob("*" + fileExt)
        df_list = (pd.read_csv(str(file)) for file in dataFiles)
        data = pd.concat(df_list, ignore_index=True)
        self.__filterUnwantedColumns(data)
        return data

    #Collect all csv files for a given game
    def getStadiumData(self, gameNr : int, fileExt : str, split : bool = False, test : bool = False):
        properFileExt = fileExt if  "." in fileExt else "." + fileExt
        dataSetPath = self.__checkParentForDesiredFolder(
            Path.cwd(),
            self.dataSetPathName,
            self.rootDirectory)
        dataSetPath = dataSetPath.joinpath(
            properFileExt.split(".")[1],
            str.format("Stadium{gameNr}Data", gameNr = gameNr),
            "Test" if test else "")
        return self.__ConverterSeperateDt(dataSetPath, properFileExt) if split else self.__ConverterAllDt(dataSetPath, properFileExt)

#main
stadConTest = PmStadiumConverter("dataSets", "pm-stat-gen-api")
dictdata = stadConTest.getStadiumData(1, "csv", True, True)
fulldtdata = stadConTest.getStadiumData(1, "csv", False, True)

#old excel version might be useful later regarding sheets manipulation
"""def Converter(self, version : int, fileExt : str, fileName : str):
    #TODO add version functionality later
    dataSetFilePath = stadConTest.__checkParentForDesiredFolder(Path.cwd(), "dataSets", "pm-stat-gen-api")
    excelFilePath = fpm.FilePathMethods.getDataSetPath(dataSetFilePath, fileExt, fileName)
    properFilePath = str(excelFilePath).replace("\\", "/")
    print("Checking Filepath:" + properFilePath)
    if (Constants.CURRENTDATASETTYPES[0]): #probably change to switch case if python
        dforg = pd.ExcelFile(properFilePath)
        wantedSheetNames = [item for item in dforg.sheet_names if "Rental" in item]
        dfrental = pd.read_excel(properFilePath, sheet_name = wantedSheetNames)
        stadConTest.__filterUnwantedColumns(dfrental)
        print("Unnecessary data removed")
        print("First row value:\n")
        #TODO here for debugging/testapp, remove when unecessary
        for cup, dFrame in dfrental.items():
            print(str.format("{cup}: {columns}", cup = cup, columns = dFrame.iloc[0]))
        return dfrental"""