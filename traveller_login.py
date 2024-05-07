from tkinter import ttk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import subprocess



class login():
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
        m_title = Label(manage_frame, text= "Login & Registration", bg= "black", fg="white", font=("times new roman", 30, "bold"))
        m_title.grid(row = 0, columnspan=2, pady= 30)


        #====name
        lbl_ID = Label(manage_frame, text= "Traveller ID", bg= "green", fg="white", font=("times new roman", 20, "bold"))
        lbl_ID.grid(row = 1, column=1, pady= 10, padx = 20,sticky= "w")
        txt_ID =Entry(manage_frame, font=("times new roman", 10, "bold"), bd= 5, relief= GROOVE)
        txt_ID.grid(row=2, column=1, pady=10, padx=30, sticky="w")

        lbl_name = Label(manage_frame, text= "Traveller Name", bg= "green", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row = 3, column=1, pady= 10, padx = 20,sticky= "w")
        txt_name =Entry(manage_frame, font=("times new roman", 20, "bold"), bd= 5, relief= GROOVE)
        txt_name.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        lbl_password = Label(manage_frame, text= "Password", bg= "green", fg="white", font=("times new roman", 20, "bold"))
        lbl_password .grid(row = 5, column=1, pady= 10, padx = 20,sticky= "w")
        txt_password =Entry(manage_frame, font=("times new roman", 20, "bold"), bd= 5, relief= GROOVE)
        txt_password.grid(row=6, column=1, pady=10, padx=10, sticky="w")



        #====detail frame

        details_frame  = Frame(self.root, bd = 4, relief= RIDGE, bg= "blue")
        details_frame.place(x =500, y = 100, width=880, height=585)

        lbl_search = Label(details_frame, text="Solent Trips", bg="gray", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")


        img = Image.open("1.jpg")
        img = img.resize((850, 540), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)



        lbl_pic = Label(details_frame, image= self.photoimg, bd=4, relief=RIDGE)
        lbl_pic.place(x=1, y=0, width = 800, height= 560)


        #====button frame

        def insert():
            subprocess.call(["python", "booking.py"])

        def add():
            subprocess.call(["python", "registration.py"])

        def new():
            subprocess.call(["python", "system_user.py"])


        btn_frame  = Frame(manage_frame, bd = 3, relief= RIDGE, bg= "white")
        btn_frame.place(x =15, y = 500, width=420)

        addbtn = Button(btn_frame, text="Submit", width=10, bg="grey", command= insert).grid(row=0, column=0, padx=10, pady=10)
        newbtn = Button(btn_frame, text="New Registration", width=20, bg="gray", command= add).grid(row=0, column=1, padx=10, pady=10)
        upbtn = Button(btn_frame, text="Login as system user", width=20, bg="gray", command= new).grid(row=0, column=2, padx=10, pady=10)






class login():
    pass
    root = Tk()
    obj= login(root)
    root.mainloop()
