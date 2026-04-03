"""
Used for handling the data to import/export
"""

import pyexcel
from dataclasses import dataclass, asdict
from typing import Any, List
from backend.typedefinitions.school import School
from enum import Enum, auto

class ExportFileType(Enum):
    """
    Enums to show the export type.
    """
    xlsx = auto()
    csv = auto()

@dataclass
class ExportColumn:
    """
    The structure for the data.
    """
    dataName: str
    dataArray: List[Any]


class ExportData:
    def __init__(self):
        self.books = {} # type: dict[str, List[ExportColumn]]
        self.currentBook = "" # type: str

    def NewBook(self, name: str, clearExisting: bool = False):
        if name not in self.books or clearExisting:
            addItem = []
        else:
            addItem = self.books[name]
        
        self.books[name] = addItem
        self.currentBook = name

    @staticmethod
    def DictToExportColumns(dictInput: dict[str, Any]) -> List[ExportColumn]:
        output = [] # type: List[ExportColumn]

        for item in dictInput:
            val = dictInput[item]
            
            exportColumn = ExportColumn(item, val)
            output.append(exportColumn)

        return output
    

    def AppendDicts(self, dictInput: dict[str, Any], book: str = ""):
        self.AppendDatas(ExportData.DictToExportColumns(dictInput), book)


    def AppendDatas(self, data: List[ExportColumn], book: str = ""):
        if book == "":
            book = self.currentBook
        
        self.books[book] = data
        
    
    def Export(self, book: str, type: ExportFileType, fullFilePath: str):
        export_dict = {column.dataName: column.dataArray for column in self.books[book]}
        extension = type.name
        full_path = f"{fullFilePath}.{extension}"
        sheet = pyexcel.get_sheet(adict=export_dict)
        sheet.save_as(full_path)

        print(f"Exported data in {full_path}")
            