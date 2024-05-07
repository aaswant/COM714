from tkinter import ttk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import subprocess

class trip():
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
        m_title = Label(manage_frame, text= "Trip Description", bg= "black", fg="white", font=("times new roman", 30, "bold"))
        m_title.grid(row = 0, columnspan=2, pady= 30)


        lbl_choose = Label(manage_frame, text="Trip type", bg="green", fg="white",
                       font=("times new roman", 20, "bold"))
        lbl_choose.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        combo_choose = ttk.Combobox(manage_frame, font=("times new roman", 13, "bold"), state='readonly')
        combo_choose['values'] = ("one-day trip", "weekend trip", "fortnight trip")
        combo_choose.grid(row=1, column=1, pady=10, padx=10)

        lbl_iden = Label(manage_frame, text="Hospitality", bg="green", fg="white",
                       font=("times new roman", 20, "bold"))
        lbl_iden.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        combo_iden = ttk.Combobox(manage_frame, font=("times new roman", 13, "bold"), state='readonly')
        combo_iden['values'] = ("Hotel", "Resort", "Camp")
        combo_iden.grid(row=2, column=1, pady=10, padx=10)

        lbl_den = Label(manage_frame, text="Point of Interest", bg="green", fg="white",
                       font=("times new roman", 20, "bold"))
        lbl_den.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        combo_den = ttk.Combobox(manage_frame, font=("times new roman", 13, "bold"), state='readonly')
        combo_den['values'] = ("museum", "historical site")
        combo_den.grid(row=3, column=1, pady=10, padx=10)


        lbl_dn = Label(manage_frame, text="Transfer point", bg="green", fg="white",
                       font=("times new roman", 20, "bold"))
        lbl_dn.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        combo_dn = ttk.Combobox(manage_frame, font=("times new roman", 13, "bold"), state='readonly')
        combo_dn['values'] = ("airport", "ferry port")
        combo_dn.grid(row=3, column=1, pady=10, padx=10)



        #====detail frame

        details_frame  = Frame(self.root, bd = 4, relief= RIDGE, bg= "blue")
        details_frame.place(x =500, y = 100, width=880, height=585)



        img = Image.open("6.jpg")
        img = img.resize((850, 540), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)



        lbl_pic = Label(details_frame, image= self.photoimg, bd=4, relief=RIDGE)
        lbl_pic.place(x=1, y=0, width = 800, height= 560)



        btn_frame = Frame(manage_frame, bd=3, relief=RIDGE, bg="white")
        btn_frame.place(x=15, y=500, width=420)
        def add():
            subprocess.call(["python", "home.py"])

        addbtn = Button(btn_frame, text="Submit", width=10, bg="grey", command=root.destroy).grid(row=0, column=0, padx=10,pady=10)
        updatebtn = Button(btn_frame, text="Home", width=10, bg="gray", command = add).grid(row=0, column=1, padx=10, pady=10)


class trip():
    pass
    root = Tk()
    obj = trip(root)
    root.mainloop()

