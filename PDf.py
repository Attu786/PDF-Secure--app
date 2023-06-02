#@aurthor @Akarshit kashyap

from fileinput import filename
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PyPDF2 import PdfFileWriter, PdfFileReader


root=Tk()
root.title("PDF Secure lock")
root.geometry("1000x700+300+100")
root.resizable(False,False)

def BROWSE():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="Select Choosen file",
                                        filetype=(('PDF File','*.pdf'),('all files','*.*'))) # type: ignore
    entry1.insert(END, filename)

def protect():
    mainfile=source.get()
    protectfile=target.get()
    code=password.get()

    if mainfile=="" and protectfile=="":
       messagebox.showerror("Inavalid!","All entries are empty!") 
    
    elif mainfile=="":
      messagebox.showerror("Invalid!","Please Type Source PDF Filename")

    elif protectfile=="":
       messagebox.showerror("Invalid!","Please Select the Target PDF File ")
    elif code=="":
       messagebox.showerror("Invalid!","Type Password ")
    
    else:
        try:
            out=PdfFileWriter()
            file = PdfFileReader(filename)
            num = file.numPages

            for idx in range(num):
                PAGES=file.getPage(idx) 
                out.addPage(PAGES) 
             #password
            out.encrypt(code)

            with open(protectfile,"wb") as f:
               out.write(f)

            source.set("")
            target.set("")
            password.set("")

            messagebox.showinfo("info","Sucessfully done")
        except:
           messagebox.showinfo("Congrats!","Your PDF is secured")
        
        
    
       
    




#ICON
image_icon=PhotoImage(file="images/icon.png") 
root.iconphoto(False,image_icon)


#main
Top_image=PhotoImage(file="images/top.png")
Label(root,image=Top_image).pack()

Frame=Frame(root, width=970,height=390,bd=5,relief=GROOVE,)
Frame.place(x=10,y=270)



##########
source=StringVar()
Label(Frame,text="Source PDF File:",font="arial 12 bold",fg="#4c4542" ).place(x=30,y=50)
entry1=Entry(Frame,width=60,textvariable=source,font="arial 15",bd=1)
entry1.place(x=170,y=48)

Button_icon=PhotoImage(file="images/search.png")
Button(Frame,image=Button_icon,width=30,height=20,bg="#d3cdcd",command=BROWSE).place(x=840,y=47)

##########
target=StringVar()
Label(Frame,text="Target PDF File:",font="arial 12 bold",fg="#4c4542" ).place(x=30,y=100)
entry2=Entry(Frame,width=60,textvariable=target,font="arial 15",bd=1)
entry2.place(x=170,y=100)

##########
password=StringVar()
Label(Frame,text="Set User Password:",font="arial 12 bold",fg="#4c4542" ).place(x=15,y=150)
entry3=Entry(Frame,width=60,textvariable=password,font="arial 15",bd=1)
entry3.place(x=170,y=150)


button_icon=PhotoImage(file="images/pdf.png")
protect=Button(root,text="Secure your PDF", compound=LEFT,image=button_icon,width=230,height=50,bg="#bfb9b9",font="arial 17 bold",command=protect)  # type: ignore
protect.pack(side=BOTTOM,pady=90)








root.mainloop()