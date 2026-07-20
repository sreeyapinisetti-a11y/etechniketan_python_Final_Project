import csv, os
from expense import Expense
HEADER=["ID","Title","Amount","Category","Date"]

def load_csv(path):
    items=[]
    if not os.path.exists(path): return items
    with open(path,newline="",encoding="utf-8") as f:
        r=csv.DictReader(f)
        for row in r:
            items.append(Expense(int(row["ID"]),row["Title"],float(row["Amount"]),row["Category"],row["Date"]))
    return items

def save_csv(path,items):
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f);w.writerow(HEADER)
        for e in items:
            w.writerow([e.id,e.title,e.amount,e.category,e.date])
