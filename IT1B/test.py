#import tkinter as tk
from tkinter import *
import qrcode
from tkinter import filedialog

okno = Tk()
okno.title("QR code generator")
e1_nadpis=Label(text="URL")
e2_nadpis=Label(text="Jméno souboru")
hotovo=Label(text="Hotovo")
e1 = Entry(okno, width=60)
e2 = Entry(okno, width=60)
e1_nadpis.pack()
e1.pack()
e2_nadpis.pack()
e2.pack()


def stisknuto():
    url=e1.get()
    jmeno=e2.get()
    png=".png"
    cesta=filedialog.askdirectory()
    img=qrcode.make(url)
    type(img)
    img.save(cesta+"/"+jmeno+png.strip())
    hotovo.pack()
    
   

tlacitko=Button(okno, text="Generovat", command=stisknuto)
tlacitko.pack()

okno.mainloop()
