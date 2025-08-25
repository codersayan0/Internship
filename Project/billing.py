from tkinter import *
from tkinter import messagebox
import random
from datetime import datetime
import os
import tempfile
from PIL import Image, ImageTk

# ============main============================
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title("Bill Book")
        self.root.configure(bg="#000000")  
        title = Label(self.root, text="ABC Restaurant",
                         font=('times new roman', 30, 'bold'),
                         pady=4, bd=12, bg="#3C138B", fg="white", relief=GROOVE)
        title.pack(fill=X)

        # ================= Variables ==================
        # Fastfood
        self.eggroll = IntVar()
        self.moglai = IntVar()
        self.noodles = IntVar()
        self.chickenroll = IntVar()
        self.momo = IntVar()
        self.pakora = IntVar()

        # Hotel Menu
        self.paneer = IntVar()
        self.friedrice = IntVar()
        self.chickencurry = IntVar()
        self.fishfry = IntVar()
        self.vegthali = IntVar()
        self.muttoncurry = IntVar()

        # Cold Drinks
        self.coke = IntVar()
        self.sprite = IntVar()
        self.thumsup = IntVar()
        self.limca = IntVar()
        self.frooti = IntVar()
        self.maaza = IntVar()

        # Total price & tax
        self.fastfood_price = StringVar()
        self.hotel_price = StringVar()
        self.cold_drink_price = StringVar()

        self.fastfood_tax = StringVar()
        self.hotel_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # Customer
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

    # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="White", bg="#3C138B")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg="#3C138B", fg="White", font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="#3C138B",fg="White", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg="#3C138B", fg="White", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

        delete_btn = Button(F1, text="Delete", command=self.delete_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        delete_btn.grid(row=0, column=7, pady=5, padx=10)                                                                   

        # ================= Fastfood Frame =================
        F2 = LabelFrame(self.root, text="Fastfood Purpose", font=('times new roman', 15, 'bold'), bd=10, fg="gold", bg="#3C138B")
        F2.place(x=5, y=180, width=370, height=380)

        food_items = [
            ("Egg Roll", self.eggroll),
            ("Moglai", self.moglai),
            ("Noodles", self.noodles),
            ("Chicken Roll", self.chickenroll),
            ("Momo", self.momo),
            ("Pakora", self.pakora)
        ]
        for i, (name, var) in enumerate(food_items):
            Label(F2, text=name, font=("times new roman", 15, "bold"), bg="#3C138B", fg="lightgreen").grid(row=i,column=0,padx=10,pady=10,sticky="w")
            Entry(F2, width=10, textvariable=var, font=("times new roman", 15, "bold"), bd=5,
                  relief=SUNKEN).grid(row=i, column=1, padx=10, pady=10)

        # ================= Hotel Menu Frame =================
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Hotel Menu", font=("times new roman", 15, "bold"),
                        fg="gold", bg="#3C138B")
        F3.place(x=385, y=180, width=365, height=380)

        hotel_items = [
            ("Paneer Masala", self.paneer),
            ("Fried Rice", self.friedrice),
            ("Chicken Curry", self.chickencurry),
            ("Fish Fry", self.fishfry),
            ("Veg Thali", self.vegthali),
            ("Mutton Curry", self.muttoncurry)
        ]
        for i, (name, var) in enumerate(hotel_items):
            Label(F3, text=name, font=("times new roman", 15, "bold"), bg="#3C138B", fg="lightgreen").grid(row=i,column=0,padx=10,pady=10,sticky="w")
            Entry(F3, width=10, textvariable=var, font=("times new roman", 15, "bold"), bd=5,
                  relief=SUNKEN).grid(row=i, column=1, padx=10, pady=10)

        # ================= Cold Drink Frame =================
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman", 15, "bold"),
                        fg="gold", bg="#3C138B")
        F4.place(x=760, y=180, width=365, height=380)

        cold_items = [
            ("Coke", self.coke),
            ("Sprite", self.sprite),
            ("Thums Up", self.thumsup),
            ("Limca", self.limca),
            ("Frooti", self.frooti),
            ("Maaza", self.maaza)
        ]
        for i, (name, var) in enumerate(cold_items):
            Label(F4, text=name, font=("times new roman", 15, "bold"), bg="#3C138B", fg="lightgreen").grid(row=i,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=10,
                                                                                                          sticky="w")
            Entry(F4, width=10, textvariable=var, font=("times new roman", 15, "bold"), bd=5,
                  relief=SUNKEN).grid(row=i, column=1, padx=10, pady=10)

        # ================= Bill Area =================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1140, y=180, width=360, height=380)

        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        # Frame for text area
        bill_text_frame = Frame(F5)
        bill_text_frame.pack(fill=BOTH, expand=1)

        scrol_y = Scrollbar(bill_text_frame, orient=VERTICAL)
        self.txtarea = Text(bill_text_frame, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(side=LEFT, fill=BOTH, expand=1)

        # Frame for QR code
        self.qr_label = Label(F5, bg="white")
        self.qr_label.pack(pady=5)



        # ================= Button Frame =================
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg="gold", bg="#3C138B")
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Fastfood Price", bg="#3C138B", fg="white",
                       font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.fastfood_price, bd=7,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Hotel Menu Price", bg="#3C138B", fg="white",
                       font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.hotel_price, bd=7,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Cold Drink Price", bg="#3C138B", fg="white",
                       font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.cold_drink_price, bd=7,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        # Taxes
        c1_lbl = Label(F6, text="Fastfood Tax", bg="#3C138B", fg="white",
                       font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.fastfood_tax, bd=7,
                       relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Hotel Menu Tax", bg="#3C138B", fg="white",
                       font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.hotel_tax, bd=7,
                       relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Cold Drink Tax", bg="#3C138B", fg="white",
                       font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.cold_drink_tax, bd=7,
                       relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        # Buttons
        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=800, width=650, height=105)

        total_btn = Button(btn_F, text="Total", command=self.total, bg="cadetblue", fg="white", pady=15, width=10,
                           bd=5, font="arial 12 bold").grid(row=0, column=0, padx=5, pady=5)
        gbill_btn = Button(btn_F, text="Generate Bill", command=self.bill_area, bg="cadetblue", fg="white", pady=15,
                           width=10, bd=5, font="arial 12 bold").grid(row=0, column=1, padx=5, pady=5)
        print_btn = Button(btn_F, text="Print", command=self.print_bill, bg="cadetblue", bd=5, fg="white", pady=15, width=10, font='arial 12 bold')
        print_btn.grid(row=0, column=2, padx=5, pady=10)
        clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", pady=15, width=10,
                           bd=5, font="arial 12 bold").grid(row=0, column=3, padx=5, pady=5)
        exit_btn = Button(btn_F, text="Exit", command=self.root.destroy, bg="cadetblue", fg="white", pady=15, width=10,
                          bd=5, font="arial 12 bold").grid(row=0, column=4, padx=5, pady=5)

        self.welcome_bill()

    # ================= Functions =================
    def total(self):
        # Fastfood
        self.total_fastfood_price = (
            (self.eggroll.get() * 50) +
            (self.moglai.get() * 70) +
            (self.noodles.get() * 60) +
            (self.chickenroll.get() * 80) +
            (self.momo.get() * 40) +
            (self.pakora.get() * 30)
        )
        self.fastfood_price.set("Rs. " + str(self.total_fastfood_price))
        self.fastfood_tax.set("Rs. " + str(round(self.total_fastfood_price * 0.05, 2)))

        # Hotel Menu
        self.total_hotel_price = (
            (self.paneer.get() * 120) +
            (self.friedrice.get() * 90) +
            (self.chickencurry.get() * 150) +
            (self.fishfry.get() * 100) +
            (self.vegthali.get() * 80) +
            (self.muttoncurry.get() * 180)
        )
        self.hotel_price.set("Rs. " + str(self.total_hotel_price))
        self.hotel_tax.set("Rs. " + str(round(self.total_hotel_price * 0.1, 2)))

        # Cold Drinks
        self.total_cold_drink_price = (
            (self.coke.get() * 40) +
            (self.sprite.get() * 40) +
            (self.thumsup.get() * 45) +
            (self.limca.get() * 35) +
            (self.frooti.get() * 25) +
            (self.maaza.get() * 30)
        )
        self.cold_drink_price.set("Rs. " + str(self.total_cold_drink_price))
        self.cold_drink_tax.set("Rs. " + str(round(self.total_cold_drink_price * 0.05, 2)))

        fastfood_tax_val = round(self.total_fastfood_price * 0.05, 2)
        hotel_tax_val = round(self.total_hotel_price * 0.1, 2)
        cold_drink_tax_val = round(self.total_cold_drink_price * 0.05, 2)

        self.total_bill = (
    self.total_fastfood_price +
    self.total_hotel_price +
    self.total_cold_drink_price +
    fastfood_tax_val +
    hotel_tax_val +
    cold_drink_tax_val
)

#==============welcome-bill==============================
    def welcome_bill(self):
        self.txtarea.delete("1.0", END)
        self.txtarea.insert(END, "\tWelcome to Foodie Hub\n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        
        now = datetime.now()
        date_time = now.strftime("%d-%m-%Y %H:%M:%S")
        self.txtarea.insert(END, f"\nDate & Time : {date_time}")

        self.txtarea.insert(END, "\n====================================")
        self.txtarea.insert(END, "\n Product\t\tQTY\tPrice")
        self.txtarea.insert(END, "\n====================================")

    def bill_area(self):
        self.total()
        if self.c_name.get().strip() == "" or self.c_phone.get().strip() == "":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.fastfood_price.get() == "Rs. 0" and self.hotel_price.get() == "Rs. 0" and self.cold_drink_price.get() == "Rs. 0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
        # Fastfood
        if self.eggroll.get() != 0:
            self.txtarea.insert(END, f"\n Egg Roll\t\t{self.eggroll.get()}\t{self.eggroll.get() * 50}")
        if self.moglai.get() != 0:
            self.txtarea.insert(END, f"\n Moglai\t\t{self.moglai.get()}\t{self.moglai.get() * 70}")
        if self.noodles.get() != 0:
            self.txtarea.insert(END, f"\n Noodles\t\t{self.noodles.get()}\t{self.noodles.get() * 60}")
        if self.chickenroll.get() != 0:
            self.txtarea.insert(END, f"\n Chicken Roll\t\t{self.chickenroll.get()}\t{self.chickenroll.get() * 80}")
        if self.momo.get() != 0:
            self.txtarea.insert(END, f"\n Momo\t\t{self.momo.get()}\t{self.momo.get() * 40}")
        if self.pakora.get() != 0:
            self.txtarea.insert(END, f"\n Pakora\t\t{self.pakora.get()}\t{self.pakora.get() * 30}")

        # Hotel Menu
        if self.paneer.get() != 0:
            self.txtarea.insert(END, f"\n Paneer Butter\t\t{self.paneer.get()}\t{self.paneer.get() * 120}")
        if self.friedrice.get() != 0:
            self.txtarea.insert(END, f"\n Fried Rice\t\t{self.friedrice.get()}\t{self.friedrice.get() * 90}")
        if self.chickencurry.get() != 0:
            self.txtarea.insert(END, f"\n Chicken Curry\t\t{self.chickencurry.get()}\t{self.chickencurry.get() * 150}")
        if self.fishfry.get() != 0:
            self.txtarea.insert(END, f"\n Fish Fry\t\t{self.fishfry.get()}\t{self.fishfry.get() * 100}")
        if self.vegthali.get() != 0:
            self.txtarea.insert(END, f"\n Vegthali\t\t{self.vegthali.get()}\t{self.vegthali.get() * 80}")
        if self.muttoncurry.get() != 0:
            self.txtarea.insert(END, f"\n Mutton Curry\t\t{self.muttoncurry.get()}\t{self.muttoncurry.get() * 180}")

        #================ColdDrinks==========================
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\n Coke\t\t{self.coke.get()}\t{self.coke.get() * 40}")
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t{self.sprite.get() * 40}")
        if self.thumsup.get() != 0:
            self.txtarea.insert(END, f"\n Thums Up\t\t{self.thumsup.get()}\t{self.thumsup.get() * 45}")
        if self.limca.get() != 0:
            self.txtarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t{self.limca.get() * 35}")
        if self.frooti.get() != 0:
            self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t{self.frooti.get() * 25}")
        if self.maaza.get() != 0:
            self.txtarea.insert(END, f"\n Maaza\t\t{self.maaza.get()}\t{self.maaza.get() * 30}")
            self.txtarea.insert(END, f"\n--------------------------------")
        # ===============taxes==============================
        if self.fastfood_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Fastfood Tax\t\t\t{self.fastfood_tax.get()}")
        if self.hotel_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Hotel Tax\t\t\t{self.hotel_tax.get()}")
        if self.cold_drink_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drink_tax.get()}")

        self.txtarea.insert(END, f"\n Total Bil:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()

        # ==== Centered Scan & Pay QR Code ====
        try:
            # Add some space
            self.txtarea.insert(END, "\n\n")

            # Configure a center tag
            self.txtarea.tag_configure("center", justify="center")
        
            # Insert only one "Scan & Pay" line centered
            self.txtarea.insert(END, "Scan & Pay\n", "center")
        
            # Load and resize QR image
            qr_image = Image.open("qr.png")
            qr_image = qr_image.resize((150, 150))
            self.qr_img = ImageTk.PhotoImage(qr_image)

            # Insert image centered
            self.txtarea.insert(END, "\n", "center")  # Start a new centered line
            self.txtarea.image_create("end", image=self.qr_img)
            self.txtarea.insert(END, "\n", "center")

            # Keep reference to prevent garbage collection
            self.txtarea.qr_ref = self.qr_img

        except Exception as e:
            print("QR Code Error:", e)



    #=========savebill============================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            if not os.path.exists("bills"):
                os.makedirs("bills")
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return
    
    # ===================delete_bill================================
    def delete_bill(self):
        if self.search_bill.get() == "":
            messagebox.showerror("Error", "Please enter a Bill Number to delete")
            return
        bill_path = f"bills/{self.search_bill.get()}.txt"
        if os.path.exists(bill_path):
            op = messagebox.askyesno("Delete", "Do you want to delete this bill?")
            if op > 0:
                os.remove(bill_path)
                messagebox.showinfo("Deleted", f"Bill no:{self.search_bill.get()} deleted successfully")
        else:
            messagebox.showerror("Error", "Bill not found")
                
# ===================find_bill================================
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")
            
    # ======================clear-bill======================
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.eggroll.set(0)
            self.moglai.set(0)
            self.noodles.set(0)
            self.chickenroll.set(0)
            self.momo.set(0)
            self.pakora.set(0)
    # ============Hotel Menu==============================
            self.paneer.set(0)
            self.friedrice.set(0)
            self.chickencurry.set(0)
            self.fishfry.set(0)
            self.vegthali.set(0)
            self.muttoncurry.set(0)
    # =============coldDrinks=============================
            self.coke.set(0)
            self.sprite.set(0)
            self.thumsup.set(0)
            self.limca.set(0)
            self.frooti.set(0)
            self.maaza.set(0)

    # ====================taxes================================
            self.fastfood_price.set("")
            self.hotel_price.set("")
            self.cold_drink_price.set("")

            self.fastfood_tax.set("")
            self.hotel_tax.set("")
            self.cold_drink_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

            if hasattr(self.txtarea, "qr_ref"):
                self.txtarea.qr_ref = None



   # ====================Print Bill============================
    def print_bill(self):
        if self.txtarea.get('1.0', END).strip() == "":
         messagebox.showerror("Error", "Bill area is empty")
         return
        else:
          temp_file = tempfile.mktemp(".txt")
          with open(temp_file, 'w') as f:
            f.write(self.txtarea.get('1.0', END))
        os.startfile(temp_file, "print")
# ====================Print Bill============================
    def print_bill(self):
        if self.txtarea.get('1.0', END).strip() == "":
         messagebox.showerror("Error", "Bill area is empty")
         return
        else:
          temp_file = tempfile.mktemp(".txt")
          with open(temp_file, 'w') as f:
            f.write(self.txtarea.get('1.0', END))
        os.startfile(temp_file, "print")
    # ===========exit=======================
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()
