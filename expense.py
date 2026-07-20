from dataclasses import dataclass

@dataclass
class Expense:
    id:int
    title:str
    amount:float
    category:str
    date:str
