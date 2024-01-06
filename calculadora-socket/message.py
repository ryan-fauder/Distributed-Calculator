import json
class Message: 
    type: str = ''
    datatype: str = ''
    data: str = ''
    datasize: int = 0

    def __init__(self, type, datatype, data, datasize) -> None:
        self.type = type
        self.datatype = datatype
        self.data = data
        self.datasize = datasize
    def __str__(self) -> str:
        return f'type: {self.type}; datatype: {self.datatype}; data: {self.data }; datasize: {self.datasize}'
    def dict(self):
        return {
            "type": self.type,
            "data": self.data,
            "datatype": self.datatype,
            "datasize": self.datasize
        }
