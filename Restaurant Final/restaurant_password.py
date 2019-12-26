from tkinter import*
import random
import time
file=open("order.txt","r")
filenew=open("order.txt","r")
list=[]
def first_page():
    a = username_entry.get()
    b = password_entry.get()
    if a == "admin" and b == "123":
        root = Tk()
        root.geometry("1200x600+0+0")
        root.title("Restaurant Management System")
        root.config(bg="orange")
        Tops = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
        Tops.pack(side=TOP)

        f1 = Frame(root, width=900, height=700, relief=SUNKEN)
        f1.pack(side=LEFT)

        f2 = Frame(root, width=400, height=700, relief=SUNKEN)
        f2.pack(side=RIGHT)
        # ------------------TIME--------------
        localtime = time.asctime(time.localtime(time.time()))
        # -----------------INFO TOP------------
        lblinfo = Label(Tops, font=('aria', 30, 'bold'), text="Restaurant Management System", fg="steel blue", bd=10,
                        anchor='w')
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(Tops, font=('aria', 20,), text=localtime, fg="steel blue", anchor=W)
        lblinfo.grid(row=1, column=0)

        # ---------------Calculator------------------
        text_Input = StringVar()
        operator = ""

        txtdisplay = Entry(f2, font=('ariel', 20, 'bold'), textvariable=text_Input, bd=5, insertwidth=7, bg="white",
                           justify='right')
        txtdisplay.grid(columnspan=4)

        def btnclick(numbers):
            global operator
            operator = operator + str(numbers)
            text_Input.set(operator)

        def clrdisplay():
            global operator
            operator = ""
            text_Input.set("")

        def eqals():
            global operator
            sumup = str(eval(operator))

            text_Input.set(sumup)
            operator = ""

        def Ref():
            x = random.randint(0, 100)
            randomRef = str(x)
            # rand.set(randomRef)

            cof = int(Fries.get())
            colfries = int(Largefries.get())
            cob = int(Burger.get())
            cofi = int(Filet.get())
            cochee = int(Cheese_burger.get())
            codr = int(Drinks.get())

            costoffries = cof * 25
            costoflargefries = colfries * 40
            costofburger = cob * 35
            costoffilet = cofi * 50
            costofcheeseburger = cochee * 50
            costofdrinks = codr * 35

            costofmeal = "Tk.", str(
                '%.2f' % (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
            PayTax = ((
                                  costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks) * 0.33)
            Totalcost = (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)
            Ser_Charge = ((
                                      costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks) / 99)
            Service = "Tk.", str('%.2f' % Ser_Charge)
            OverAllCost = "Tk.", str('%.2f' % (PayTax + Totalcost + Ser_Charge))
            PaidTax = "Tk.", str('%.2f' % PayTax)

            Service_Charge.set(Service)
            cost.set(costofmeal)
            Tax.set(PaidTax)
            Subtotal.set(costofmeal)
            Total.set(OverAllCost)

        def qexit():
            root.destroy()

        def reset():
            rand.set(0)
            Fries.set(0)
            Largefries.set(0)
            Burger.set(0)
            Filet.set(0)
            Subtotal.set(0)
            Total.set(0)
            Service_Charge.set(0)
            Drinks.set(0)
            Tax.set(0)
            cost.set(0)
            Cheese_burger.set(0)

        btn7 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="7", bg="cyan",
                      command=lambda: btnclick(7))
        btn7.grid(row=2, column=0)

        btn8 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="8", bg="powder blue",
                      command=lambda: btnclick(8))
        btn8.grid(row=2, column=1)

        btn9 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="9", bg="powder blue",
                      command=lambda: btnclick(9))
        btn9.grid(row=2, column=2)

        Addition = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="+", bg="powder blue",
                          command=lambda: btnclick("+"))
        Addition.grid(row=2, column=3)
        # ---------------------------------------------------------------------------------------------
        btn4 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="4", bg="powder blue",
                      command=lambda: btnclick(4))
        btn4.grid(row=3, column=0)

        btn5 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="5", bg="powder blue",
                      command=lambda: btnclick(5))
        btn5.grid(row=3, column=1)

        btn6 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="6", bg="powder blue",
                      command=lambda: btnclick(6))
        btn6.grid(row=3, column=2)

        Substraction = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="-",
                              bg="powder blue", command=lambda: btnclick("-"))
        Substraction.grid(row=3, column=3)
        # -----------------------------------------------------------------------------------------------
        btn1 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="1", bg="powder blue",
                      command=lambda: btnclick(1))
        btn1.grid(row=4, column=0)

        btn2 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="2", bg="powder blue",
                      command=lambda: btnclick(2))
        btn2.grid(row=4, column=1)

        btn3 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="3", bg="powder blue",
                      command=lambda: btnclick(3))
        btn3.grid(row=4, column=2)

        multiply = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="*", bg="powder blue",
                          command=lambda: btnclick("*"))
        multiply.grid(row=4, column=3)
        # ------------------------------------------------------------------------------------------------
        btn0 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="0", bg="powder blue",
                      command=lambda: btnclick(0))
        btn0.grid(row=5, column=0)

        btnc = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="c", bg="powder blue",
                      command=clrdisplay)
        btnc.grid(row=5, column=1)

        btnequal = Button(f2, padx=16, pady=16, bd=4, width=16, fg="black", font=('ariel', 20, 'bold'), text="=",
                          bg="powder blue", command=eqals)
        btnequal.grid(columnspan=4)

        Decimal = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text=".", bg="powder blue",
                         command=lambda: btnclick("."))
        Decimal.grid(row=5, column=2)

        Division = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="/", bg="powder blue",
                          command=lambda: btnclick("/"))
        Division.grid(row=5, column=3)
        status = Label(f2, font=('aria', 15, 'bold'), width=16, text="My Restaurant", bd=2, relief=SUNKEN)
        status.grid(row=7, columnspan=3)

        # ---------------------------------------------------------------------------------------
        rand = StringVar()
        Fries = StringVar()
        Largefries = StringVar()
        Burger = StringVar()
        Filet = StringVar()
        Subtotal = StringVar()
        Total = StringVar()
        Service_Charge = StringVar()
        Drinks = StringVar()
        Tax = StringVar()
        cost = StringVar()
        Cheese_burger = StringVar()

        lblreference = Label(f1, font=('aria', 16, 'bold'), text="Order No.", fg="steel blue", bd=10, anchor='w')
        lblreference.grid(row=0, column=0)
        txtreference = Entry(f1, font=('ariel', 16, 'bold'), textvariable=rand, bd=6, insertwidth=4, bg="powder blue",
                             justify='right')
        txtreference.grid(row=0, column=1)

        lblfries = Label(f1, font=('aria', 16, 'bold'), text="Fries Meal", fg="steel blue", bd=10, anchor='w')
        lblfries.grid(row=1, column=0)
        txtfries = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Fries, bd=6, insertwidth=4, bg="powder blue",
                         justify='right')
        txtfries.grid(row=1, column=1)

        lblLargefries = Label(f1, font=('aria', 16, 'bold'), text="Lunch Meal", fg="steel blue", bd=10, anchor='w')
        lblLargefries.grid(row=2, column=0)
        txtLargefries = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Largefries, bd=6, insertwidth=4,
                              bg="powder blue", justify='right')
        txtLargefries.grid(row=2, column=1)

        lblburger = Label(f1, font=('aria', 16, 'bold'), text="Burger Meal", fg="steel blue", bd=10, anchor='w')
        lblburger.grid(row=3, column=0)
        txtburger = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Burger, bd=6, insertwidth=4, bg="powder blue",
                          justify='right')
        txtburger.grid(row=3, column=1)

        lblFilet = Label(f1, font=('aria', 16, 'bold'), text="Pizza Meal", fg="steel blue", bd=10, anchor='w')
        lblFilet.grid(row=4, column=0)
        txtFilet = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Filet, bd=6, insertwidth=4, bg="powder blue",
                         justify='right')
        txtFilet.grid(row=4, column=1)

        lblCheese_burger = Label(f1, font=('aria', 16, 'bold'), text="Cheese burger", fg="steel blue", bd=10, anchor='w')
        lblCheese_burger.grid(row=5, column=0)
        txtCheese_burger = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Cheese_burger, bd=6, insertwidth=4,
                                 bg="powder blue", justify='right')
        txtCheese_burger.grid(row=5, column=1)

        # --------------------------------------------------------------------------------------
        lblDrinks = Label(f1, font=('aria', 16, 'bold'), text="Drinks", fg="steel blue", bd=10, anchor='w')
        lblDrinks.grid(row=0, column=2)
        txtDrinks = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg="powder blue",
                          justify='right')
        txtDrinks.grid(row=0, column=3)

        lblcost = Label(f1, font=('aria', 16, 'bold'), text="Cost", fg="steel blue", bd=10, anchor='w')
        lblcost.grid(row=1, column=2)
        txtcost = Entry(f1, font=('ariel', 16, 'bold'), textvariable=cost, bd=6, insertwidth=4, bg="powder blue",
                        justify='right')
        txtcost.grid(row=1, column=3)

        lblService_Charge = Label(f1, font=('aria', 16, 'bold'), text="Service Charge", fg="steel blue", bd=10, anchor='w')
        lblService_Charge.grid(row=2, column=2)
        txtService_Charge = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Service_Charge, bd=6, insertwidth=4,
                                  bg="powder blue", justify='right')
        txtService_Charge.grid(row=2, column=3)

        lblTax = Label(f1, font=('aria', 16, 'bold'), text="Tax", fg="steel blue", bd=10, anchor='w')
        lblTax.grid(row=3, column=2)
        txtTax = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Tax, bd=6, insertwidth=4, bg="powder blue",
                       justify='right')
        txtTax.grid(row=3, column=3)

        lblSubtotal = Label(f1, font=('aria', 16, 'bold'), text="Subtotal", fg="steel blue", bd=10, anchor='w')
        lblSubtotal.grid(row=4, column=2)
        txtSubtotal = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Subtotal, bd=6, insertwidth=4, bg="powder blue",
                            justify='right')
        txtSubtotal.grid(row=4, column=3)

        lblTotal = Label(f1, font=('aria', 16, 'bold'), text="Total", fg="steel blue", bd=10, anchor='w')
        lblTotal.grid(row=5, column=2)
        txtTotal = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Total, bd=6, insertwidth=4, bg="powder blue",
                         justify='right')
        txtTotal.grid(row=5, column=3)

        count1 = 0
        # file_read=file.read()
        for i in filenew:
            # print(str(i))
            # g=i
            if count1 == 0:
                rand.set(i)
                g = i
                count1 = count1 + 1
            elif count1 == 1:
                Fries.set(i)
                count1 = count1 + 1

            elif count1 == 2:
                Largefries.set(i)
                count1 = count1 + 1

            elif count1 == 3:
                Burger.set(i)
                count1 = count1 + 1

            elif count1 == 4:
                Filet.set(i)
                count1 = count1 + 1
            elif count1 == 5:
                Cheese_burger.set(i)
                count1 = count1 + 1

            elif count1 == 6:
                Drinks.set(i)
                count1 = count1 + 1

        #count1 = 0
        # -----------------------------------------buttons------------------------------------------
        lblTotal = Label(f1, text="---------------------", fg="white")
        lblTotal.grid(row=6, columnspan=3)

        btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="TOTAL",
                          bg="powder blue", command=Ref)
        btnTotal.grid(row=7, column=1)

        btnreset = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="RESET",
                          bg="powder blue", command=reset)
        btnreset.grid(row=7, column=2)

        btnexit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="EXIT",
                         bg="powder blue", command=qexit)
        btnexit.grid(row=7, column=3)

        def price():
            fr1 = Tk()
            fr1.title("Menu")
            fr1.geometry("300x200")
            fr1.configure(background='yellow')
            list = Frame(fr1)
            list.grid()

            pizza = Label(list, text="Pizza")
            pizza.grid(row=3)
            piz = IntVar(list)
            pizza_entry = Entry(list, textvariable=piz)  # textvariable=var
            pizza_entry.grid(row=3, column=2)

            # pizza_button=Button(list,text="+",command=increase(var))
            # pizza_button.grid(row=0,column=3)
            bur = IntVar(list)
            burger = Label(list, text="Burger")
            burger.grid(row=2)
            burger_entry = Entry(list, textvariable=bur)
            burger_entry.grid(row=2, column=2)

            chi = IntVar(list)
            chicken = Label(list, text="Fries Meal")
            chicken.grid(row=0)
            chicken_entry = Entry(list, textvariable=chi)
            chicken_entry.grid(row=0, column=2)

            dri = IntVar(list)
            juice = Label(list, text="Drinks")
            juice.grid(row=5)
            juice_entry = Entry(list, textvariable=dri)
            juice_entry.grid(row=5, column=2)

            lun = IntVar(list)
            lunch = Label(list, text="Lunch")
            lunch.grid(row=1)
            lunch_entry = Entry(list, textvariable=lun)
            lunch_entry.grid(row=1, column=2)

            che = IntVar(list)
            cheese = Label(list, text="Cheese")
            cheese.grid(row=4)
            cheese_entry = Entry(list, textvariable=che)
            cheese_entry.grid(row=4, column=2)

            ord = StringVar(list)
            order = Label(list, text="Order Number")
            order.grid(row=6)
            order_entry = Entry(list, textvariable=ord)
            order_entry.grid(row=6, column=2)

            submit = Button(list, fg="green", text="Submit")  # , command=placed())
            submit.grid()

            count = 0
            # file_read=file.read()
            for i in file:
                # print(str(i))
                # g=i
                if count == 0:
                    ord.set(i)
                    g = i
                    count = count + 1
                elif count == 1:
                    chi.set(i)
                    count = count + 1

                elif count == 2:
                    lun.set(i)
                    count = count + 1

                elif count == 3:
                    bur.set(i)
                    count = count + 1

                elif count == 4:
                    che.set(i)
                    count = count + 1
                elif count == 5:
                    dri.set(i)
                    count = count + 1

                elif count == 6:
                    piz.set(i)
                    count = count + 1

            fr1.mainloop()

        btnprice = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="MENU",
                          bg="powder blue", command=price)
        btnprice.grid(row=7, column=0)
        root.mainloop()
    else:
        # count=1
        # print (count)
        lbl_wrong = Label(app, text="Wrong Username or Password")
        lbl_wrong.grid(row=4, column=2)
        # count=count+1


root1=Tk()
root1.title("Burger King")
#root.configure(background='grey')
root1.geometry("800x400")

#root.mainloop()
app=Frame(root1)
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
root1.mainloop()