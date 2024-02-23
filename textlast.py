from transformers import VitsModel, AutoTokenizer
import torch
from IPython.display import Audio
import scipy
from tkinter import *
import tkinter as tk


def play():
    text = entry.get()
    speed = variable.get()
    speed = speed.replace("x","")
    
    try:
 
        readText(text,speed)
        print("Okudum")
         
    except:
      print("write a text in text box.")
        





def readText(text,rate):

    model = VitsModel.from_pretrained("facebook/mms-tts-tur")
    tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-tur")
    text = str(text)
    inputs = tokenizer(text, return_tensors="pt")
    print(model.config.sampling_rate)
    with torch.no_grad():
        output= model(**inputs).waveform
    Audio(output, rate = model.config.sampling_rate)
    output_np = output.cpu().numpy()
    output_np = np.int16(output_np * 32767)
    scipy.io.wavfile.write("techno.wav", rate = model.config.sampling_rate, data = output_np)




def get_vol(val):
    print("sa")

master = Tk()
master.title('TextToSpeech')
master.geometry('750x200')
master.config(bg = '#000000')

variable = StringVar(master)
speeds = ["0.5x", "1.0x", "2.0x"]
variable.set(speeds[1])


optionMenu = OptionMenu(master, variable, *speeds)
optionMenu.config(width=40, bg = "#ff0000")
optionMenu.place(x=370,y = 60)

scale = Scale(master, from_=0, to = 100, orient=HORIZONTAL, command=get_vol)
scale.config(bg = "#ff0000")
scale.set(50)
scale.place(x = 325, y = 150)

entry = tk.Entry(font = "Verdana 14",width=59, bg = "#ff0000") 
entry.place(x=20,y=20)

buton = tk.Button(text="PLAY",command=play,width=40, bg = "#ff0000")
buton.place(x=200,y=110)




master.mainloop()
