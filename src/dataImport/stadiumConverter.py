import pandas as pd
import sys
from pathlib import Path

#If this doesn't show how BAD the module system in python is I don't know what will!
curPath = Path.cwd()
if (curPath.name == "pm-stat-gen-api"):
    sys.path.append(str(curPath))
elif (curPath.name == "src"):
    sys.path.append(str(curPath.parent))
elif (curPath.name == "stadiumConverter"):
    sys.path.append(str(curPath.parent.parent))
import src.common.filePathMethods as fpm

DESIREDCOLUMNS = [ #potentially move this to csv/json file
    "Pokemon", "Level", 
    "Type 1", "Type 2", 
    "Move 1", "Move 2", "Move 3", "Move 4",
    "HP Stat", "Attack Stat", "Defense Stat", "Special Stat", "Special Attack Stat", "Special Defense Stat", "Speed Stat",
    "Attack DV", "Defense DV", "Special DV", "Speed DV",
    "HP IV", "Attack IV", "Defense IV", "Special Attack IV", "Special Defense IV", "Speed IV"
]

class PmStadiumConverter():
    def __init__(self):
       pass

    def __checkParentForDesiredFolder(self, curDir : Path, desiredFolderName : str, limitFolderName : str):
        for folder in curDir.iterdir():
            if desiredFolderName in folder.name:
                return folder
        if limitFolderName in curDir.name:
            return "Desired folder not found" #TODO change this to return exception later
        self.__checkParentForDesiredFolder(curDir.parent)

    def __filterUnwantedColumns(self, data : dict):
        for dFrame in data.values():
            for column in dFrame.columns:
                if column not in DESIREDCOLUMNS:
                    del dFrame[column]
    
    def Converter(self, version : int, fileExt : str, fileName : str):
        #TODO add version functionality later
        dataSetFilePath = stadConTest.__checkParentForDesiredFolder(Path.cwd(), "dataSets", "pm-stat-gen-api")
        excelFilePath = fpm.FilePathMethods.getDataSetPath(dataSetFilePath, fileExt, fileName)
        properFilePath = str(excelFilePath).replace("\\", "/")
        print("Checking Filepath:" + properFilePath)
        if (fpm.CURRENTDATASETTYPES[0]):
            dforg = pd.ExcelFile(properFilePath)
            wantedSheetNames = [item for item in dforg.sheet_names if "Rental" in item]
            dfrental = pd.read_excel(properFilePath, sheet_name = wantedSheetNames)
            stadConTest.__filterUnwantedColumns(dfrental)
            print("Unnecessary data removed")
            print("First row value:\n")
            #TODO here for debugging/testapp, remove when unecessary
            for cup, dFrame in dfrental.items():
                print(str.format("{cup}: {columns}", cup = cup, columns = dFrame.iloc[0]))
            return dfrental

#main        
stadConTest = PmStadiumConverter()
stadConTest.Converter(1, "xlsx", "testDataStadium1")