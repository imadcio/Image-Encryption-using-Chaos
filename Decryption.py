from tkinter import *
from tkinter import filedialog
import os
import HenonDecryption as hD
from PIL import ImageTk, Image

def choose_File():
    filename = filedialog.askopenfilename()
    entry1.insert(0,str(filename))


def decryptHenonManipulation():
    filename = entry1.get()
    resImage = hD.decryptHenonImage(filename)
    entry3.insert(0,resImage)
    #print(filename)


def openFileForHenon():
    window = Toplevel(root)
    window.title("Henon Map")
    window.geometry("600x600")
    path = entry3.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

#from tkFileDialog import askopenfilename

root =Tk()
Frame1 = Frame(root)
Frame1.pack()


Frame4= Frame(root)
Frame4.pack(side=TOP)


label_1 = Label(Frame1, text ="Image to be Decrypted : ",width = 125)
entry1 = Entry(Frame1,width =100)
button1 = Button(Frame1, text = "Select Image",command = choose_File)

button4 = Button(Frame4, text="Decrypt Henon Map",command = decryptHenonManipulation,width=20)
entry3 = Entry(Frame4,width =80)
button5 = Button(Frame4, text="Open Image",command = openFileForHenon)


label_1.pack(side = TOP)
entry1.pack(side = TOP)
button1.pack(side = TOP)


button4.pack(side = LEFT)
entry3.pack(side = LEFT)
button5.pack(side = LEFT)

root.mainloop()
