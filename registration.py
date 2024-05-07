from tkinter import *
import cv2
from PIL import Image, ImageTk
import subprocess
from tkinter import ttk




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
        m_title = Label(manage_frame, text= "Registration", bg= "black", fg="white", font=("times new roman", 30, "bold"))
        m_title.grid(row = 0, columnspan=2, pady= 30)
        #====name
        lbl_name = Label(manage_frame, text= "Traveller Name", bg= "green", fg="white", font=("times new roman", 10, "bold"))
        lbl_name.grid(row = 1, column=0, pady= 10, padx = 20,sticky= "w")
        txt_name =Entry(manage_frame, font=("times new roman", 10, "bold"), bd= 5, relief= GROOVE)
        txt_name.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        #===== ADDRESS

        lbl_address = Label(manage_frame, text="Traveller Address", bg="green", fg="white",
                         font=("times new roman", 10, "bold"))
        lbl_address.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        self.txt_address = Text(manage_frame, width=30, height = 3, font=("times new roman", 10, "bold"))
        self.txt_address.grid(row=2, column=1, pady=10, padx=10, sticky="w")


        #====DATE OF BIRTH

        lbl_dob = Label(manage_frame, text="Traveller date 0f birth", bg="green", fg="white",
                         font=("times new roman", 10, "bold"))
        lbl_dob.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_dob = Entry(manage_frame, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=3, column=1, pady=10, padx=10, sticky="w")
        #==== contact number

        lbl_number = Label(manage_frame, text="Traveller contact details", bg="green", fg="white",
                         font=("times new roman", 10, "bold"))
        lbl_number.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txt_number= Entry(manage_frame, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_number.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        #===== ID
        lbl_ID = Label(manage_frame, text="Traveller ID", bg="green", fg="white",
                         font=("times new roman", 10, "bold"))
        lbl_ID.grid(row=5, column=0, pady=10, padx=20, sticky="w")


        combo_ID = ttk.Combobox( manage_frame, font =("times new roman", 13, "bold"), state= 'readonly')
        combo_ID['values'] = ("passport", "driving license", "national identity card", "others")
        combo_ID.grid(row=5, column=1, pady=10, padx=10)


        lbl_ID_no = Label(manage_frame, text="ID_NO", bg="green", fg="white",
                         font=("times new roman", 10, "bold"))
        lbl_ID_no.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_ID_no= Entry(manage_frame, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_ID_no.grid(row=6, column=1, pady=10, padx=10, sticky="w")

        # ====detail frame

        details_frame = Frame(self.root, bd=4, relief=RIDGE, bg="blue")
        details_frame.place(x=500, y=100, width=880, height=585)


        img = Image.open("3.jpg")
        img = img.resize((850, 540), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_pic = Label(details_frame, image= self.photoimg, bd=4, relief=RIDGE)
        lbl_pic.place(x=1, y=0, width = 800, height= 560)

        # ====button frame
        def add():
            subprocess.call(["python", "booking.py"])

        btn_frame = Frame(manage_frame, bd=3, relief=RIDGE, bg="white")
        btn_frame.place(x=15, y=500, width=420)


        addbtn = Button(btn_frame, text="Submit", width=20, bg="grey", command=add).grid(row=0, column=1, padx=10,pady=10)





class login():
    pass
    root = Tk()
    obj= login(root)
    root.mainloop()
