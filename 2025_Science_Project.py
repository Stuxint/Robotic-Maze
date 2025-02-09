import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
import os

root = tk.Tk()
root.geometry("387x422")
root.resizable(False, False)
root.title("Robotic Maze")

photo = "C:\\Users\\natha\\OneDrive\\Pictures\\Screenshots\\Screenshot 2025-02-09 150039.png"

if os.path.exists(photo): #check if file exists before trying to load
    try:
        icon = tk.PhotoImage(file=photo)
        root.iconphoto(False, icon)
    except tk.TclError as e:
        print(f"Error loading icon: {e}")
else:
    print(f"Icon not found at {photo}")
 
fon = font.Font(family="Courier", size=12)
menubar = tk.Menu()

def lve():
    image = Image.open("C:\\Users\\natha\\OneDrive\\Pictures\\Screenshots\\Screenshot 2025-01-25 142810.png").resize((350,350))
    img = ImageTk.PhotoImage(image)

    canvas2 = tk.Canvas(root)
    canvas2.place(x=20, y=20, width=350, height=350)
    canvas2.create_image( 0, 0, image = img, anchor = "nw")
    

    iagahs = Image.open("C:\\Users\\natha\\OneDrive\\Pictures\\Screenshots\\Screenshot 2025-02-03 144405.png").resize((40,40))
    ia = ImageTk.PhotoImage(iagahs)

    global canvas11
    canvas11 = tk.Canvas(root)
    canvas11.place(x=20, y=323, width=40, height=40)
    canvas11.create_image( 0, 0, image = ia, anchor = "nw") 
    root.bind("<w>", b1)
    root.bind("<s>", b2)
    root.bind("<a>", b3)
    root.bind("<d>", b4)
    root.configure(bg="lightgreen")

    butto = tk.Button(root, text="Reset")
    butto.config(command=h)
    butto.place(x=330, y=372)
#Controls
def b1(event):
    canvas11.place(x=canvas11.winfo_x(), y=canvas11.winfo_y()-10)
def b2(event):
    canvas11.place(x=canvas11.winfo_x(), y=canvas11.winfo_y()+10)
def b3(event):
    canvas11.place(x=canvas11.winfo_x()-10, y=canvas11.winfo_y())
def b4(event):
    canvas11.place(x=canvas11.winfo_x()+10, y=canvas11.winfo_y())
def h():
    canvas11.place(x=20, y=323, width=40, height=40)

def lv():
    image = Image.open("C:\\Users\\natha\\OneDrive\\Pictures\\Screenshots\\Screenshot 2025-01-26 160447.png").resize((350,350))
    img = ImageTk.PhotoImage(image)
    
    canvas2 = tk.Canvas(root)
    canvas2.place(x=20, y=20, width=350, height=350)
    canvas2.create_image( 0, 0, image = img, anchor = "nw") 
    

    iagahs = Image.open("C:\\Users\\natha\\OneDrive\\Pictures\\Screenshots\\Screenshot 2025-02-03 144405.png").resize((40,40))
    ia = ImageTk.PhotoImage(iagahs)

    global canvas1
    canvas1 = tk.Canvas(root)
    canvas1.place(x=25, y=320, width=40, height=40)
    canvas1.create_image( 0, 0, image = ia, anchor = "nw")
    root.bind("<w>", a1)
    root.bind("<s>", a2)
    root.bind("<a>", a3)
    root.bind("<d>", a4)
    root.configure(bg="yellow")

    butto = tk.Button(root, text="Reset")
    butto.config(command=hi)
    butto.place(x=330, y=372)

#Controls
def a1(event):
    canvas1.place(x=canvas1.winfo_x(), y=canvas1.winfo_y()-10)
def a2(event):
    canvas1.place(x=canvas1.winfo_x(), y=canvas1.winfo_y()+10)
def a3(event):
    canvas1.place(x=canvas1.winfo_x()-10, y=canvas1.winfo_y())
def a4(event):
    canvas1.place(x=canvas1.winfo_x()+10, y=canvas1.winfo_y())
def hi():
    canvas1.place(x=25, y=320, width=40, height=40)


def l():
    image = Image.open("C:\\Users\\natha\\OneDrive\\Pictures\\Screenshots\\Screenshot 2025-01-28 142345.png").resize((350,350))
    img = ImageTk.PhotoImage(image)
    
    canvas2 = tk.Canvas(root)
    canvas2.place(x=20, y=20, width=350, height=350)
    canvas2.create_image( 0, 0, image = img, anchor = "nw")
   
    iagahs = Image.open("C:\\Users\\natha\\OneDrive\\Pictures\\Screenshots\\Screenshot 2025-02-03 144405.png").resize((30,30))
    ia = ImageTk.PhotoImage(iagahs)

    global canvas12
    canvas12 = tk.Canvas(root)
    canvas12.place(x=30, y=325, width=30, height=30)
    canvas12.create_image( 0, 0, image = ia, anchor = "nw") 
    root.bind("<w>", c1)
    root.bind("<s>", c2)
    root.bind("<a>", c3)
    root.bind("<d>", c4)
    root.configure(bg="red")
    butto = tk.Button(root, text="Reset")
    butto.config(command=i)
    butto.place(x=330, y=372)

#Controls
def c1(event):
    canvas12.place(x=canvas12.winfo_x(), y=canvas12.winfo_y()-10)
def c2(event):
    canvas12.place(x=canvas12.winfo_x(), y=canvas12.winfo_y()+10)
def c3(event):
    canvas12.place(x=canvas12.winfo_x()-10, y=canvas12.winfo_y())
def c4(event):
    canvas12.place(x=canvas12.winfo_x()+10, y=canvas12.winfo_y())
def i():
    canvas12.place(x=30, y=325, width=30, height=30)

#Menubar
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Choose Your Lvl", menu=file_menu)
file_menu.add_command(label="Lvl 1", background='lightgreen', command=lve, font=fon)
file_menu.add_command(label="Lvl 2", background='yellow', command=lv, font=fon)
file_menu.add_command(label="Lvl 3", background='red', command=l, font=fon)
root.config(menu=menubar)




root.mainloop()