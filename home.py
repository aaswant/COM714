from tkinter import ttk
from tkinter import *

from PIL import Image, ImageTk
import subprocess


class home():
    def __init__(self, root):
        self.root = root
        self.root.title("Travel management system")
        self.root.geometry("1370x700+0+0")

        title = Label(self.root, text = "Travel management system", bd=9, relief = GROOVE, font =("Algerian", 50, "bold"), bg= "black", fg= "white")
        title.pack(side=TOP, fill=X)



        #===== frame generating
        manage_frame  = Frame(self.root, bd = 4, relief= RIDGE, bg= "red")
        manage_frame.place(x =20, y = 100, width=450, height= 585)


        #====heading
        m_title = Label(manage_frame, text= "SOLENT TRIPS", bg= "black", fg="white", font=("times new roman", 30, "bold"))
        m_title.grid(row = 0, columnspan=2, pady= 30)

        # ===== ID
        lbl_choose = Label(manage_frame, text="Explore", bg="green", fg="white",
                       font=("times new roman", 30, "bold"))
        lbl_choose.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        combo_choose = ttk.Combobox(manage_frame, font=("times new roman", 13, "bold"), state='readonly')
        combo_choose['values'] = ("System Users", "Traveller")
        combo_choose.grid(row=2, column=1, pady=10, padx=10)


        img1 = Image.open("4.jpg")
        img = img1.resize((850, 540), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl_pic_1 = Label(manage_frame, image= self.photoimg1, bd=4, relief=RIDGE)
        lbl_pic_1.place(x=100, y=290, width = 300, height= 200)




        #====detail frame

        details_frame  = Frame(self.root, bd = 4, relief= RIDGE, bg= "blue")
        details_frame.place(x =500, y = 100, width=880, height=585)



        img = Image.open("5.jpg")
        img = img.resize((850, 540), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)



        lbl_pic = Label(details_frame, image= self.photoimg, bd=4, relief=RIDGE)
        lbl_pic.place(x=1, y=0, width = 800, height= 560)


        def add():
            subprocess.call(["python", "traveller_login.py"])

        btn_frame  = Frame(manage_frame, bd = 3, relief= RIDGE, bg= "white")
        btn_frame.place(x =15, y = 500, width=420)

        addbtn = Button(btn_frame, text="Submit", width=10, bg="grey", command= add).grid(row=0, column=0, padx=10, pady=10)


class home():
    pass
    root = Tk()
    obj= home(root)
    root.mainloop()
