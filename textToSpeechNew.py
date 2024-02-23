from tkinter import *
import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

def play():
    text = entry.get()
    speed = variable.get()
    lang = variable2.get()
    speed = speed.replace("x","")
    
    try:
 
        readTextEn(text,speed,lang)
        print("Okudum")
         
    except:
      print("write a text in text box.")
        


def readTextEn(text,speed, lang):
    
    speedRate = speed * 100
    engine.setProperty("rate", speedRate)
    voices = engine.getProperty('voices')
    if lang=="TR":
        engine.setProperty('voice', voices[64].id)
    else:
        engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def get_vol(val):
    engine.setProperty('volume', val)



master = Tk()
master.title('TextToSpeech')
master.geometry('750x200')
master.config(bg = '#000000')

variable = StringVar(master)
speeds = ["0.5x", "1.0x", "2.0x"]
variable.set(speeds[1])

variable2 = StringVar(master)
langs = ["TR", "EN"]
variable2.set(langs[0])


optionMenu = OptionMenu(master, variable, *speeds)
optionMenu.config(width=40, bg = "#ff0000")
optionMenu.place(x=370,y = 60)

optionMenu2 = OptionMenu(master, variable2, *langs)
optionMenu2.config(width=40, bg = "#ff0000")
optionMenu2.place(x=20,y = 60)

scale = Scale(master, from_=0, to = 100, orient=HORIZONTAL, command=get_vol)
scale.config(bg = "#ff0000")
scale.set(50)
scale.place(x = 325, y = 150)

entry = tk.Entry(font = "Verdana 14",width=59, bg = "#ff0000") 
entry.place(x=20,y=20)

buton = tk.Button(text="PLAY",command=play,width=40, bg = "#ff0000")
buton.place(x=200,y=110)




master.mainloop()
