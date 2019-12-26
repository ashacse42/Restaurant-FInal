
from tkinter import *
from tkinter import messagebox

file=open("order.txt","r")
list=[0]
"""def increase(var):
    m=list[0]
    m=m+1
    x = var.get() + 1
    var.set(x+m)
    list[0]=list[0]+1"""


def first_page():

    a=username_entry.get()
    b=password_entry.get()
    if a=="admin" and b=="123":
        fp = Tk()
        fp.title("Menu")
        fp.geometry("300x300")
        fp.configure(background='yellow')
        list_fp = Frame(fp)
        list_fp.grid()
        lbl_list = Label(list_fp, text="Welcome! to Burger King")
        lbl_list.grid(row=0, column=6)
        bttn1 = Button(list_fp, text="Order", command=menu_list)
        bttn1.grid(row=1, column=6)

        bttn2 = Button(list_fp, text="Total Bill")
        bttn2.grid(row=2, column=6)

        bttn3 = Button(list_fp, text="Invoice")
        bttn3.grid(row=3, column=6)
        button = Button(list_fp, text="QUIT", fg="red", command=quit)
        button.grid(row=4, column=6)
        fp.mainloop()
    else:
        #count=1
        #print (count)
        lbl_wrong=Label(app,text="Wrong Username or Password")
        lbl_wrong.grid(row=4,column=2)
        #count=count+1


def menu_list():
    fr1=Tk()
    fr1.title("Menu")
    fr1.geometry("300x200")
    fr1.configure(background='yellow')
    list=Frame(fr1)
    list.grid()

    pizza=Label(list,text="Pizza")
    pizza.grid(row=3)
    piz = IntVar(list)
    pizza_entry=Entry(list,textvariable=piz) #textvariable=var
    pizza_entry.grid(row=3,column=2)

    #pizza_button=Button(list,text="+",command=increase(var))
    #pizza_button.grid(row=0,column=3)
    bur = IntVar(list)
    burger=Label(list,text="Burger")
    burger.grid(row=2)
    burger_entry=Entry(list,textvariable=bur)
    burger_entry.grid(row=2,column=2)

    chi = IntVar(list)
    chicken=Label(list,text="Fries Meal")
    chicken.grid(row=0)
    chicken_entry=Entry(list,textvariable=chi)
    chicken_entry.grid(row=0,column=2)

    dri=IntVar(list)
    juice=Label(list,text="Drinks")
    juice.grid(row=5)
    juice_entry=Entry(list,textvariable=dri)
    juice_entry.grid(row=5,column=2)

    lun = IntVar(list)
    lunch=Label(list,text="Lunch")
    lunch.grid(row=1)
    lunch_entry=Entry(list,textvariable=lun)
    lunch_entry.grid(row=1,column=2)

    che = IntVar(list)
    cheese=Label(list,text="Cheese")
    cheese.grid(row=4)
    cheese_entry=Entry(list,textvariable=che)
    cheese_entry.grid(row=4,column=2)

    ord = StringVar(list)
    order=Label(list,text="Order Number")
    order.grid(row=6)
    order_entry=Entry(list,textvariable=ord)
    order_entry.grid(row=6,column=2)

    #submit=Button(list,fg="green",text="Submit",command=placed())
    #submit.grid()


    count=0
    #file_read=file.read()
    for i in file:
        #print(str(i))
        #g=i
        if count==0:
            ord.set(i)
            g=i
            count=count+1
        elif count==1:
            chi.set(i)
            count = count + 1

        elif count==2:
            lun.set(i)
            count = count + 1

        elif count==3:
            bur.set(i)
            count = count + 1

        elif count==4:
            che.set(i)
            count = count + 1
        elif count==5:
            dri.set(i)
            count = count + 1

        elif count==6:
            piz.set(i)
            count = count + 1

    fr1.mainloop()
def placed():
    result1 = messagebox.askyesno("Confirm", "Confirm?")
    if result1 == True:
        messagebox.showinfo("Order"," Order has been placed.")
    else:
        pass
root=Tk()
root.title("Burger King")
#root.configure(background='grey')
root.geometry("800x400")

#root.mainloop()
app=Frame(root)
app.grid()
username=Label(app,fg="red",text="Username").grid(row=0,column=0)

username_entry=Entry(app)
username_entry.grid(row=0,column=1)
password=Label(app,fg="red",text="Password")
password.grid(row=1,column=0)
password_entry=Entry(app,show="*")
password_entry.grid(row=1,column=1)
login=Button(app,fg="green",font="bold",text="Login",command=first_page)
login.grid(row=2,column=1)
root.mainloop()