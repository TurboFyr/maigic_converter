#Tyler Martel
#My GUI Converter
#6/20/22//7/14/22

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Tyler's Magical Converter")
frm = ttk.Frame (root, padding=25)
frm.grid()

def convert():
    x=choices.get()
    if x==('F to C'):
        a=int(inbox.get())
        celsius=(((a)-32)*5/9)
        outbox.insert(0, celsius)
    else:
         if x==('KPH to MPH'):
                a=int(inbox.get())
                mph=a/1.609
                outbox.insert(0,mph)
         if x==('MPH to KNOT'):
               a=int(inbox.get())
               knot=a/1.151
               outbox.insert(0,knot)
         if x==('KG to LB'):
               a=int(inbox.get())
               lb=a*2.204
               outbox.insert(0,lb)
         if x==('mA to Amp'):
               a=int(inbox.get())
               Amp=(a*.001)
               outbox.insert(0,Amp)
         if x==('mS to Sec'):
                a=int(inbox.get())
                Sec=(a*.001)
                outbox.insert(0,Sec)


myv=['F to C','KPH to MPH', 'MPH to KNOT','KG to LB','CM to IN','mA to Amp',
     'mS to Sec'
    ]

chlabel=ttk.Label(frm,text="\u2193What to convert?\u2193")
outlabel=ttk.Label (frm, text='Converted Measure --->')

choices=ttk.Combobox(frm, values=myv)
choices.current(0)

abutton=Button(frm, activebackground='red',text='Convert!', command=convert)
inbox=ttk.Entry(frm, width=14)
outbox=ttk.Entry(frm,width=14)


chlabel.grid(column=0, row=0)
inbox.grid(column=1, row=1)
outbox.grid(column=1, row=2)
outlabel.grid(column=0, row=2)
abutton.grid(column=2,row=1)
choices.grid(column=0, row=1)
mainloop()
