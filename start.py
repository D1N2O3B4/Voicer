from tkinter import Tk, messagebox, PhotoImage, Label, StringVar, Entry, Button
from scipy.io.wavfile import write
import wavio as wv
import sounddevice as sound
import time

app = Tk()

#Window Shape
app.geometry("600x700+450+80")
app.resizable(False,False)
app.title("Voicer")
app.configure(background="#4a4a4a")

#Record Function
def Record():
    freq = 44100
    dur = int(duration.get())
    recording = sound.rec(dur*freq, samplerate = freq, channels = 2)
    
    #Timer
    try:
        temp = int(duration.get())
    except:
        raise Exception("You need to put in a value!!")
    
    while temp > 0:
        app.update()
        time.sleep(1)
        temp -= 1

        if temp == 0:
            messagebox.showinfo("Time Countdown","Your time is up!")
        
        Label(text=f"{str(temp)}",font="arial 20",width=4,background="#4a4a4a").place(x=240,y=590)

    sound.wait()
    write("recording.wav",freq,recording)


#icon
img_icon = PhotoImage(file="./assets/record.png")
app.iconphoto(False,img_icon)

#image
pic = PhotoImage(file="./assets/recordbtn.png")
myimage = Label(image=pic,background="#4a4a4a")
myimage.pack(pady=150)

#entrybox
duration = StringVar()
entry = Entry(app,textvariable=duration,font="arial 20",width=10).pack(pady=10)

#button
record = Button(app,font="arial 20", text="Record", bg="#111111",fg="white",border=0).pack(pady=30)


app.mainloop()