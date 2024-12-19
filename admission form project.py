
import tkinter
from tkinter import *
from tkinter import messagebox
root=tkinter.Tk()

root.title("GTP Collage")
root.geometry("900x800")
header=Label(root,text="Gajmal Tulshiram Patil",font=("",20))
lb1=Label(root,text="Enter your name : ",font=("",20),pady=15)
lb2=Label(root,text="Enter your address : ",font=("",20),pady=15)
lb3=Label(root,text="Mobile number : ",font=("",20),pady=15)
lb4=Label(root,text="Select Gender : ",font=("",20),pady=15)
lb5=Label(root,text="Select Year : ",font=("",20),pady=15)
e1=Entry(root,font=("",20))#name
e2=Text(root,width=36,height=5)#addres
e3=Entry(root,font=("",20))#mobile number

mfg=StringVar()
gdr=StringVar()


#radiobutton
genderm=Radiobutton(root,text=("Male"),font=("",20),variable=mfg,value="MALE") #radiobuton for gender
genderf=Radiobutton(root,text=("Female"),font=("",20),variable=mfg,value="FEMALE")
#genderf=Radiobutton(root,text=("Female"),font=("",20),variable=gdr,value="F")

def selyr():
    if gdr.get()=="1":
        lbx1.delete(0,END)
        lbx1.insert(0,'Maths')
        lbx1.insert(0,'english')
    elif gdr.get()=="2":
        lbx1.delete(0,END)
        lbx1.insert(0,'physics')
        lbx1.insert(0,'chemistry')
    elif gdr.get()=="3":
        lbx1.delete(0,END)
        lbx1.insert(0,'geometry')
        lbx1.insert(0,'algebra')
        
fy=Radiobutton(root,text=("FY"),font=("",20),variable=gdr,value="1",command=selyr)
sy=Radiobutton(root,text=("SY"),font=("",20),variable=gdr,value="2",command=selyr)
ty=Radiobutton(root,text=("TY"),font=("",20),variable=gdr,value="3",command=selyr)

lbx1=Listbox(root,font=("",20),height=5,selectmode=MULTIPLE) #listbox
    
#pack
header.grid(row=0,column=0,columnspan=2)
lb1.grid(row=1,column=0,sticky="W")
lb2.grid(row=2,column=0)
lb3.grid(row=3,column=0,sticky="W")
lb4.grid(row=4,column=0,columnspan=2)
lb5.grid(row=6,column=0,columnspan=2)

e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)

genderm.grid(row=5,column=0)
genderf.grid(row=5,column=1)
fy.grid(row=7,column=0)
sy.grid(row=7,column=1)
ty.grid(row=7,column=2)

lbx1.grid(row=8,column=1)



def saveinfo():
    for i in lbx1.curselection():
        selsub=lbx1.get(i)
    
    f1=open('admissionform.txt','w')
    f1.write('Name: '+e1.get()+'\n')
    f1.write('Address: '+e2.get('1.0','end')+'\n')
    f1.write('Contact no: '+e3.get()+'\n')
    f1.write('gender :'+mfg.get()+'\n')
    f1.write('year : '+gdr.get())
    f1.write('selected subs : '+selsub)
    
    f1.close()
 
btn=Button(root,text="Save Info",font=("",20),command=saveinfo).grid(row=9,column=1) #button
#print(year.get)

root.mainloop()
