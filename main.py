from expense_tracker import ExpenseTracker
t=ExpenseTracker()
while True:
    print("\n1.Add\n2.View\n3.Search\n4.Update\n5.Delete\n6.Summary\n7.Exit")
    c=input("Choice: ")
    if c=="1": t.add()
    elif c=="2": t.view()
    elif c=="3": t.search()
    elif c=="4": t.update()
    elif c=="5": t.delete()
    elif c=="6": t.summary()
    elif c=="7":
        t.save();print("Saved.");break
    else: print("Invalid")
