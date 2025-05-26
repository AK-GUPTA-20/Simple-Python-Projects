from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfWriter, PdfReader
import os
from PIL import ImageTk, Image

root = Tk()
root.title("Pdf Protector")
root.geometry("700x460+300+100")
root.resizable(False, False)

def browse():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select PDF File",
                                          filetype=(("PDF File", '*.pdf'), ('all files', '*.*')))
    entry1.insert(END, filename)

def protectfile():
    mainfile = source.get()
    protectfile = target.get()
    code = password.get()
    
    if mainfile == '' and protectfile == '' and code == '':
        messagebox.showerror("Invalid", "All entries are empty!")
    
    elif mainfile == '':
        messagebox.showerror("Invalid", "Please select the Source PDF File!")     
        
    elif protectfile == "":
        messagebox.showerror("Invalid", "Please type/select Target PDF Filename!")   
    
    elif code == "":
        messagebox.showerror("Invalid", "Please type the Password!")
    
    else:
        try:
            out = PdfWriter()
            file = PdfReader(mainfile)
            num = len(file.pages)
            
            for idx in range(num):
                page = file.pages[idx]
                out.add_page(page)
                
            out.encrypt(code)
            
            with open(protectfile, 'wb') as f:
                out.write(f)
            
            source.set("")
            target.set("")
            password.set("")
            messagebox.showinfo("Success", "PDF file successfully protected!")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Change background color
root.configure(bg="lightblue")

# Add icon 
root.iconbitmap("Password protect file/icon.ico")

# Add image
img_open = Image.open("Password protect file/top image.png")
resize_img = img_open.resize((700, 115))
img = ImageTk.PhotoImage(resize_img)
img_label = Label(image=img)
img_label.pack()

# Adding the frame
frame = Frame(root, width=680, height=320, bd=5, relief=GROOVE)
frame.place(x=10, y=130)

#####   (1)
source = StringVar()
Label(frame, text="Source PDF file:", font="arial 12 bold", fg="#4c4542").place(x=30, y=50)
entry1 = Entry(frame, width=30, textvariable=source, font='arial 18', bd=1)
entry1.place(x=200, y=48)

btn_icn = PhotoImage(file="Password protect file/button image.png")
Button(frame, image=btn_icn, width=35, height=25, bg="#d3cdcd", command=browse).place(x=605, y=47)

#####   (2)
target = StringVar()
Label(frame, text="Target PDF file:", font="arial 12 bold", fg="#4c4542").place(x=30, y=100)
entry2 = Entry(frame, width=30, textvariable=target, font='arial 18', bd=1)
entry2.place(x=200, y=100)

#######   (3)
password = StringVar()
Label(frame, text="Set User Password:", font="arial 12 bold", fg="#4c4542").place(x=30, y=150)
entry3 = Entry(frame, width=30, textvariable=password, font='arial 18', bd=1)
entry3.place(x=200, y=150)

button_icon = PhotoImage(file="Password protect file/button.png")
protect = Button(root, text="Protect PDF File...", image=button_icon, width=250, height=50, bg="#bfb9b9", font='arial 18 bold', compound=LEFT, command=protectfile)
protect.pack(side=BOTTOM, pady=40)

# Adding icon at the corner
corner_icon = PhotoImage(file="Password protect file/corner.png")
corner_label = Label(frame, image=corner_icon)
corner_label.place(x=635, y=277)

root.mainloop()
