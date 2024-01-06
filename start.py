from tkinter import Tk, messagebox, PhotoImage, Label, StringVar, Entry, Button

app = Tk()

#Window Shape
app.geometry("600x700+450+80")
app.resizable(False,False)
app.title("Voicer")
app.configure(background="#4a4a4a")

def Record():
    freq = 44100
    

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