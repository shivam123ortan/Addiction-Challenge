import tkinter
from tkinter import Tk,Label
from tkinter import *
from datetime import *
import random


root = Tk()
root.geometry('700x500')

# title
root.title('Break Bad Habbit')
root.configure(bg='black')

label1 = Label(root,text='<< In India,Alcohol kills 2.6L and nearly 1.35 million deaths every year. >>',font="lucida 14 bold",bg='black',fg = 'white',pady=10)
label2 = Label(root,text='One Indian dies every 96 minutes due to alcohol consumption.A number of cities in the country \nhave banned alcohol production and sale since reports suggest that the number of deaths \ncaused by alcohol are on a hike.So now lets say "GOOD BYE TOBACCO AND ALCOHAL"',
               font='lucida 13',bg='light green',fg = 'black',pady=10)

label3 = Label(root,text='|| Overcoming Alcohol Addiction ||',bg='black',fg='red',pady=10,padx=10, font="lucida 16 bold")
label4 = Label(root,text='|| Overcoming Smoke Addiction ||',bg='black',fg='red',pady=10,padx=10, font="lucida 16 bold")


# Button
Abutton = Button(root,text='Click here',bg='black',fg='white',font="lucida 20 bold",command=lambda :alcohol(n()))
Sbutton = Button(root,text='Click here',bg='black',fg='white',font="lucida 20 bold",command=lambda :call(n()+1))

# Grid


label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=6,column=0)
label4.grid(row=8,column=0)
Abutton.grid(row=7)
Sbutton.grid(row=9)

def n():
    try:
        f = open("date.txt", "r+")
        l = f.read()
        d = date.today()
        y,m,t = l.split(',')
        l = date(int(y),int(m),int(t))
        n = d - l
    except:
        f = open("date.txt", "w")
        y,m,d = str(date.today()).split('-')
        f.write(f"{y},{m},{d}")
        f.close()
        n = 0
    return n.days


#FUNCTIONS
def smoke_day(n):
    return "<<< Day" + " " + str(n) + " " + "Mission >>>"

def back(t):
    t.destroy()


def mission(n):
    missions = {1:"\ 10 minutes Meditation in Morning /\n\ Write your today's time table on your diary /",
                2:"\ Start walking in the morning /\n\ Meet with your loved ones /",
                3:"\ Run for 1KM in Morning /\n\ Spend time with reading at least 10 pages of Inspirational Book /",
                4:"\ Run for 2KM. /\n\ Do deep breathing yoga. /",
                5:"\ Run for 3KM /\n\ Create a new Habit which you love to do /\n\ Read 10 Pages of a book /",
                6:"\ Do stretching exercises /\n\ Do 20 minutes Meditation /",
                7:"\ Run for 3KM /\n\ Movie Night /",
                8:"\ Do Yoga for 20 minutes /\n\ 20 Push-ups /",}
    return missions.get(n)

#QUOTES
quotes = ["The positive health effects of quitting smoking begin 20 minutes after your last cigarette. \nYour blood pressure and pulse will start to return to more normal levels.",
        "Within eight hours, your carbon monoxide levels will return to a more normal level. \nCarbon monoxide is a chemical present in cigarette smoke that replaces oxygen particles in the blood, \nlowering the amount of oxygen your tissues receive.",
        "By the one-day mark, you’ve already decreased your risk of heart attack. \nThis is because of reduced constriction of veins and arteries as well as increased oxygen levels that \ngo to the heart to boost its functioning",
        "At 48 hours, previously damaged nerve endings start to regrow. You may also start to notice \nthat senses that were previously dulled due to smoking improve. You may realize you’re \nsmelling and tasting things better than you were before",
        "Within three days after quitting smoking, you’ll often find yourself breathing more easily. \nThis is because the bronchial tubes inside the lungs have started to relax and open up \nmore. This makes air exchange between carbon dioxide and oxygen easier.",
        "The one-week milestone is important not only for your health, but for your success rate in \nquitting smoking successfully long term. Smokers who successfully make it one week without \nsmoking are nine times as likely to successfully quit.",
        "Within two weeks of quitting smoking, you may start to notice you’re not only breathing easier. \nYou’re also walking easier. This is thanks to improved circulation and oxygenation.",
        "In just one short month, you can experience many health changes related to stopping smoking. \nOne is feeling a sense of heightened overall energy.",
        "Within three months after quitting, a woman can improve her fertility as well as \nreduce the risk that her baby will be born prematurely",
        "After six months of quitting, many people often notice they’re better able to \nhandle stressful events that come their way without feeling like they need to smoke."]


def call(n):
    t = Toplevel()

    # TOP THINGS
    t.title("Smoke")
    t.configure(bg="black")
    t.geometry("780x400")

    # BACK BUTTON
    bb = Button(t, text="< Back", font="lucida 11 bold", bg="black", fg="white", command=lambda : back(t))
    bb.grid(row=0, column=0)

    # MISSIONS
    mi = StringVar()
    mi.set(mission(n))
    m_day = Label(t,textvariable=mi, bg="black", fg="white", font="lucida 15 bold")
    m_day.grid(row=4, column=1)

    # MISSION DAY
    day = StringVar()
    day.set(smoke_day(n))
    day1 = Label(t,textvariable=day, bg="black", fg="white", pady=40, font="lucida 15 bold")
    day1.grid(row=3, column=1)

    #quote
    quote = StringVar()
    rand = random.randint(1, 9)
    quote.set(quotes[rand])
    quote_banner = Label(t,textvariable=quote, bg="black", fg="white", font="lucida 11 bold")
    quote_banner.grid(row=1, column=1)

    # TIP BANNER
    tip = Label(t,text="TIPS!!!", bg="black", fg="white", font="lucida 15 bold")
    tip.grid(row=0, column=1)

div = IntVar()
div.set(10)
i = IntVar()
d=150

# main funtion
def alcohol(n):
    s = Toplevel()
    s.geometry("700x350")
    s.configure(bg='black')
    f = open('drink.txt', 'r')
    q = [str(x) for x in f]
    ran(s,q)
    l2 = Label(s,bg='black',fg='white',text= cal(n,q[7]),font="lucida 15 bold")
    Button(s, text="Back", bg="black", fg="white", font="lucida 13", command=lambda: bac(s,f)).grid(row=0, column=0)
    l1 = Label(s, bg='black', fg='white', text="Today's drink limit", font="lucida 15 bold")
    l3 = Label(s,bg='black',fg='white',text="mL",font="lucida 15 bold")
    Button(s, text="Relax", bg="black", fg="white", font="lucida 13", command=lambda: setdiv()).grid(row=0, column=2)
    l1.grid(row=3, column=4, columnspan=4)
    l2.grid(row=4, column=4)
    l3.grid(row=5, column=4)
    print(n)

#print quote
def ran(s,q):
    r= random.randrange(0,7,1)
    a =Label(s,text=q[r],bg='black',fg='#33B5E5', font="lucida 15 bold")
    a.place(anchor=CENTER)
    a.grid(row=1,column=4)

#calculate the max drinking volume allowed
def cal(n,d):
    c = n//7
    qua = int(d) - c*n/div.get()
    if qua < 10:
        return 0
    return qua

# Button for submission of drink capacity
def but(t,e):
    i.set(int(e.get()))
    t.destroy()

#change div
def setdiv():
    div.set(10)

#back
def bac(s,f):
    f.close()
    s.destroy()

mainloop()