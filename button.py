#Import all the necessary libraries
"""
from tkinter import *

#Define the tkinter instance
win= Toplevel()
win.title("Rounded Button")

#Define the size of the tkinter frame
win.geometry("700x300")

#Define the working of the button

def my_command():
   text.config(text= "You have clicked Me...")

#Import the image using PhotoImage function
click_btn= PhotoImage(file=r'F:/forest.jpg')

#Let us create a label for button event
img_label= Label(image=click_btn)

#Let us create a dummy button and pass the image
button= Button(win, image=click_btn,command= my_command,
borderwidth=0)
button.pack(pady=30)

text= Label(win, text= "")
text.pack(pady=30)

win.mainloop()"""
#Import tkinter library
from tkinter import *
from PIL import Image,ImageTk
#Create an instance of Tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
#Define a function to close the window
def close_win():
   win.destroy()
#Load the image
image = Image.open(r'F:/forest.jpg')
#Resize the Image
image = image.resize((150,100), Image.ANTIALIAS)
#Convert the image to PhotoImage
img= ImageTk.PhotoImage(image)
#Create a Label
Label(win, text="Click the below button to close the window",font=('Aerial 15 bold')).pack(pady=20)
#Create a label with the image
button= Button(win, text="Click Me",font= ('Helvetica 15 bold'),image=img, compound= LEFT, command=close_win)
button.pack()
win.mainloop()

