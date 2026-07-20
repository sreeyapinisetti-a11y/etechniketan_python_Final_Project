from datetime import datetime
from expense import Expense
from storage import load_csv,save_csv
from utils import valid_date

class ExpenseTracker:
    def __init__(self,file="expenses.csv"):
        self.file=file
        self.expenses=load_csv(file)
    def _next(self):
        return max([e.id for e in self.expenses],default=100)+1
    def add(self):
        t=input("Title: ")
        while True:
            try:a=float(input("Amount: "));break
            except:print("Invalid amount")
        c=input("Category: ")
        while True:
            d=input("Date (DD-MM-YYYY blank=today): ")
            if not d:
                d=datetime.now().strftime("%d-%m-%Y");break
            if valid_date(d):break
            print("Invalid date")
        e=Expense(self._next(),t,a,c,d)
        self.expenses.append(e)
        print("Added ID",e.id)
    def view(self):
        print(f"{'ID':<5}{'Title':<20}{'Amount':<10}{'Category':<15}Date")
        for e in self.expenses:
            print(f"{e.id:<5}{e.title:<20}{e.amount:<10.2f}{e.category:<15}{e.date}")
    def find(self,i):
        return next((e for e in self.expenses if e.id==i),None)
    def search(self):
        try:i=int(input("ID: "))
        except:return
        print(self.find(i))
    def update(self):
        try:i=int(input("ID: "))
        except:return
        e=self.find(i)
        if not e: print("Not found");return
        x=input(f"Title[{e.title}]: ");e.title=x or e.title
        x=input(f"Amount[{e.amount}]: ")
        if x:
            try:e.amount=float(x)
            except:pass
        x=input(f"Category[{e.category}]: ");e.category=x or e.category
        x=input(f"Date[{e.date}]: ")
        if x and valid_date(x): e.date=x
    def delete(self):
        try:i=int(input("ID: "))
        except:return
        e=self.find(i)
        if e:self.expenses.remove(e)
    def summary(self):
        total=sum(e.amount for e in self.expenses)
        print("Grand Total:",total)
        print("Records:",len(self.expenses))
        cats={}
        for e in self.expenses: cats[e.category]=cats.get(e.category,0)+e.amount
        for k,v in cats.items(): print(k,v)
    def save(self):
        save_csv(self.file,self.expenses)
