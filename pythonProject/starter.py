from tkinter import *
import guzheng as gz
import erhu as dz
from PIL import ImageTk, Image

win = Tk()
win.geometry("720x480")
win.configure(background="lightblue")
win.title("Somatosensory_Instrument")


def guzheng():
    gz.main()


def erhu():
    dz.main()


my_img = ImageTk.PhotoImage(Image.open("logo.png"))
my_label = Label(image=my_img)
my_label.place(x=300, y=80)

Label(win, text="Somatosensory_Instrument", font="Georgia 12", background="white").place(x=280, y=20)
Label(win, text="Author: Ting Jiang, Zhuohao Zeng, Mulang Shi", font="Georgia 7", background="lightblue").place(x=280, y=400)
Label(win, text="Credit: Google Mediapipe, Kazuhito Takahashi", font="Georgia 7", background="lightblue").place(x=280, y=415)
Button(win, text="Cyber Guzheng", width="12", height="1", activebackground="skyblue", bg="white",
       font="Georgia 12", command=guzheng).place(x=200, y=300)
Button(win, text="Sci-Fi Erhu", width="12", height="1", activebackground="skyblue", bg="white",
       font="Georgia 12", command=erhu).place(x=450, y=300)

win.mainloop()
