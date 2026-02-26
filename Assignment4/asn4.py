# asn4 Program

import tkinter
from PIL import Image, ImageTk

class ASN4:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("ASN4")
        self.main_window.minsize(400,300)

        # Frames
        self.img_frame = tkinter.Frame(self.main_window)
        self.img_frame.pack()
        
        self.rbdBtn_frame = tkinter.Frame(self.main_window)
        self.rbdBtn_frame.pack()

        # images
        self.img1 = Image.open("chicken.jpg")
        self.img1 = self.img1.resize((400, 300))
        self.imgOne = ImageTk.PhotoImage(self.img1)

        self.img2 = Image.open("pie.jpg")
        self.img2 = self.img2.resize((400, 300))
        self.imgTwo = ImageTk.PhotoImage(self.img2)

        self.img3 = Image.open("pizza.jpg")
        self.img3 = self.img3.resize((350, 300))
        self.imgThree = ImageTk.PhotoImage(self.img3)

        self.img4 = Image.open("steak.jpg")
        self.img4 = self.img4.resize((300, 300))
        self.imgFour = ImageTk.PhotoImage(self.img4)

        # Label
        self.lbl = tkinter.Label(self.img_frame, image = self.imgOne)
        self.lbl.pack()

        # IntVar
        self.var = tkinter.IntVar()
        self.var.set(1)

        #Radiobuttons
        self.radio_a = tkinter.Radiobutton(
            self.rbdBtn_frame,
            text = "Chicken",
            variable = self.var,
            value = 1,
            command=self.on_radio_select
        )
        self.radio_a.pack(side = "left",padx = 10)
        self.radio_b= tkinter.Radiobutton(
            self.rbdBtn_frame,
            text="Pie",
            variable = self.var,
            value = 2,
            command = self.on_radio_select
        )
        self.radio_b.pack(side = "left", padx = 10)

        self.radio_c = tkinter.Radiobutton(
            self.rbdBtn_frame,
            text = "Pizza",
            variable = self.var,
            value = 3,
            command=self.on_radio_select
        )
        self.radio_c.pack(side = "left", padx = 10)

        self.radio_d = tkinter.Radiobutton(
            self.rbdBtn_frame,
            text = "Steak",
            variable = self.var,
            value = 4,
            command = self.on_radio_select
        )
        self.radio_d.pack(side = "left", padx = 10)






        # Enter the tkinter main loop
        tkinter.mainloop()

    def on_radio_select(self):
        choice = self.var.get()
        if choice == 1:
            self.lbl.config(image = self.imgOne)
        elif choice == 2:
            self.lbl.config(image = self.imgTwo)
        elif choice == 3:
            self.lbl.config(image = self.imgThree)
        elif choice == 4:
            self.lbl.config(image = self.imgFour)

    
# Create an instance of ASN4 GUI
if __name__ == '__main__':
    show_info = ASN4()