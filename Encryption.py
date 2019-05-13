from tkinter import *
from tkinter import filedialog
import os
import ImageTransformation as iT
from PIL import ImageTk, Image

def choose_File():
    filename = filedialog.askopenfilename()
    entry1.insert(0,str(filename))


def performHenonManipulation():
    filename = entry1.get()
    resImage = iT.pixelManipulation(512, filename)
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
topFrame = Frame(root)
topFrame.pack()


bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


label_1 = Label(topFrame, text ="Image to be Encrypted : ",width = 125)
entry1 = Entry(topFrame,width =100)
button1 = Button(topFrame, text = "Select Image",command = choose_File)


button4 = Button(bottomFrame, text="Generate Henon Map",command = performHenonManipulation,width=20)
entry3 = Entry(bottomFrame,width =80)
button5 = Button(bottomFrame, text="Open Image",command = openFileForHenon)


label_1.pack(side = TOP)
entry1.pack(side = TOP)
button1.pack(side = TOP)


button4.pack(side = LEFT)
entry3.pack(side = LEFT)
button5.pack(side = LEFT)

root.mainloop()
