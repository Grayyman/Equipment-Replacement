#Import the required libraries
from tkinter import *
import tkinter.messagebox

#Create an instance of a tkinter window, set the size and name it
root = Tk()
root.title("EQUIPMENT REPLACEMENT")
root.geometry("1500x600+0+0")

#Creating the text variables for each entry box so that the .get & .set method can be used
FirsttxtInpWC = StringVar()
SecondtxtInpWC = StringVar()
ThirdtxtInpWC = StringVar()
FourthtxtInpWC = StringVar()
FifthtxtInpWC = StringVar()
FirsttxtDef = StringVar()
SecondtxtDef = StringVar()
ThirdtxtDef = StringVar()
FourthtxtDef = StringVar()
FifthtxtDef = StringVar()
FirsttxtChalng = StringVar()
SecondtxtChalng = StringVar()
ThirdtxtChalng = StringVar()
FourthtxtChalng = StringVar()
FifthtxtChalng = StringVar()
Norm1= StringVar()
Norm2= StringVar()
Norm3= StringVar()
Norm4= StringVar()
Norm5= StringVar()
Norm6= StringVar()
Norm7= StringVar()
Norm8= StringVar()
Norm9= StringVar()
Norm10= StringVar()
VONE= StringVar()
VTWO= StringVar()

#Creating empty lists to store data gotten from entry boxes for easy mathematical manipulation   
listInpWC = []
listDef = []
listchalng = []
MVC = [] 

#Creating the command function for the submit button of the input weight of criteria entry boxes
def submit_txtInpWC():
    sub_txtInpWC1 = FirsttxtInpWC.get()
    sub_txtInpWC1 = float(sub_txtInpWC1)
    sub_txtInpWC2 = SecondtxtInpWC.get()
    sub_txtInpWC2 = float(sub_txtInpWC2)
    sub_txtInpWC3 = ThirdtxtInpWC.get()
    sub_txtInpWC3 = float(sub_txtInpWC3)
    sub_txtInpWC4 = FourthtxtInpWC.get()
    sub_txtInpWC4 = float(sub_txtInpWC4)
    sub_txtInpWC5 = FifthtxtInpWC.get()
    sub_txtInpWC5 = float(sub_txtInpWC5)
    listInpWC.extend((sub_txtInpWC1,sub_txtInpWC2,sub_txtInpWC3,sub_txtInpWC4,sub_txtInpWC5))
    submit_InpWC['state'] = DISABLED
    

#Creating the command function for the submit button of the defender and challenger entry boxes
def submit_txtChalng():
    #using the global keyword to allow objects created in a function to be usable outside the function
    global sub_txtchlng1
    global sub_txtchlng2
    global sub_txtchlng3
    global sub_txtchlng4
    global sub_txtchlng5
    
    global sub_txtdef1
    global sub_txtdef2
    global sub_txtdef3
    global sub_txtdef4
    global sub_txtdef5
    
    #Getting the inputed numbers from the entry boxes in text format and converting the numbers to float
    sub_txtchlng1 = FirsttxtChalng.get()
    sub_txtchlng1 = float(sub_txtchlng1)
    sub_txtchlng2 = SecondtxtChalng.get()
    sub_txtchlng2 = float(sub_txtchlng2)
    sub_txtchlng3 = ThirdtxtChalng.get()
    sub_txtchlng3 = float(sub_txtchlng3)
    sub_txtchlng4 = FourthtxtChalng.get()
    sub_txtchlng4 = float(sub_txtchlng4)
    sub_txtchlng5 = FifthtxtChalng.get()
    sub_txtchlng5 = float(sub_txtchlng5)
    listchalng.extend((sub_txtchlng1,sub_txtchlng2,sub_txtchlng3,sub_txtchlng4,sub_txtchlng5))
    sub_txtdef1 = FirsttxtDef.get()
    sub_txtdef1 = float(sub_txtdef1)
    sub_txtdef2 = SecondtxtDef.get()
    sub_txtdef2 = float(sub_txtdef2)
    sub_txtdef3 = ThirdtxtDef.get()
    sub_txtdef3 = float(sub_txtdef3)
    sub_txtdef4 = FourthtxtDef.get()
    sub_txtdef4 = float(sub_txtdef4)
    sub_txtdef5 = FifthtxtDef.get()
    sub_txtdef5 = float(sub_txtdef5)
    listDef.extend((sub_txtdef1,sub_txtdef2,sub_txtdef3,sub_txtdef4,sub_txtdef5))
    for i in range(0,5):
        if listDef[i]>listchalng[i]:
            MVC.append(listDef[i])
        else:
            MVC.append(listchalng[i])
    submit_challenge['state'] = DISABLED
    
#Creating the command function for the normalise button
def normalise_x():
    #Setting the globalvariables
    global nd1
    global nd2
    global nd3
    global nd4
    global nd5
    global nc1
    global nc2
    global nc3
    global nc4
    global nc5
    nd1 = sub_txtdef1/MVC[0]
    Norm1.set(nd1)
    nc1 = sub_txtchlng1/MVC[0]
    Norm6.set(nc1)
    nd2 = sub_txtdef2/MVC[1]
    Norm2.set(nd2)
    nc2 = sub_txtchlng2/MVC[1]
    Norm7.set(nc2)
    nd3 = sub_txtdef3/MVC[2]
    Norm3.set(nd3)
    nc3 = sub_txtchlng3/MVC[2]
    Norm8.set(nc3)
    nd4 = sub_txtdef4/MVC[3]
    Norm4.set(nd4)
    nc4 = sub_txtchlng4/MVC[3]
    Norm9.set(nc4)
    nd5 = sub_txtdef5/MVC[4]
    Norm5.set(nd5)
    nc5 = sub_txtchlng5/MVC[4]
    Norm10.set(nc5)
    normalisee['state'] = DISABLED

#Creating the command function for the reset button
def reset_x():
   FirsttxtInpWC.set("") 
   SecondtxtInpWC.set("")
   ThirdtxtInpWC.set("")
   FourthtxtInpWC.set("")
   FifthtxtInpWC.set("")
   FirsttxtDef.set("")
   SecondtxtDef.set("")
   ThirdtxtDef.set("")
   FourthtxtDef.set("")
   FifthtxtDef.set("")
   FirsttxtChalng.set("")
   SecondtxtChalng.set("")
   ThirdtxtChalng.set("")
   FourthtxtChalng.set("")
   FifthtxtChalng.set("")
   Norm1.set("")
   Norm2.set("")
   Norm3.set("")
   Norm4.set("")
   Norm5.set("")
   Norm6.set("")
   Norm7.set("")
   Norm8.set("")
   Norm9.set("")
   Norm10.set("")
   VONE.set("")
   VTWO.set("")
   listInpWC.clear()
   listchalng.clear()
   MVC.clear()
   listDef.clear()
   
   emptylbl.destroy()
   
   submit_InpWC['state'] = NORMAL
   submit_challenge['state'] = NORMAL
   normalisee['state'] = NORMAL
   score['state'] = NORMAL

#Creating the command function for the score button
def score_x():
    global sc1
    global sc2
    global emptylbl
    sc1 = (listInpWC[0]*nd1)+(listInpWC[1]*nd2)+(listInpWC[2]*nd3)+(listInpWC[3]*nd4)+(listInpWC[4]*nd5)
    VONE.set(sc1)
    sc2 = (listInpWC[0]*nc1)+(listInpWC[1]*nc2)+(listInpWC[2]*nc3)+(listInpWC[3]*nc4)+(listInpWC[4]*nc5)
    VTWO.set(sc2)
    if sc1>sc2:
        emptylbl = Label(root,font=('arial',10,'bold'),bd=12,text=f'The Defender is the most optimal descision to go for due to a higher score of {sc1} using Simple Additive Weighting Method')
        emptylbl.grid(row=36,column=1,rowspan=10,columnspan=10,padx=10,pady=10)
    else:
        emptylbl = Label(root,font=('arial',10,'bold'),bd=12,text=f'The Challenger is the most optimal descision to go for due to a higher score of {sc2} using Simple Additive Weighting Method')
        emptylbl.grid(row=36,column=1,rowspan=10,columnspan=10,padx=10,pady=10)
    score['state'] = DISABLED   
    

#Creating the entry boxes for the "INPUT WEIGHT OF CRITERIA" values and packing it to the root window
lblInpWC = Label(root, text="INPUT WEIGHT OF CRITERIA", font=('arial',10,'bold'),bd=12)
lblInpWC.grid(row=0,column=0,padx=10,pady=10)
txtInpWC1 = Entry(root, textvariable=FirsttxtInpWC, font=('arial',10,'bold'),bd=1)
txtInpWC1.grid(row=0,column=1,padx=10,pady=10)
txtInpWC2 = Entry(root, textvariable=SecondtxtInpWC, font=('arial',10,'bold'),bd=1)
txtInpWC2.grid(row=0,column=2,padx=10,pady=10)
txtInpWC3 = Entry(root, textvariable=ThirdtxtInpWC, font=('arial',10,'bold'),bd=1)
txtInpWC3.grid(row=0,column=3,padx=10,pady=10)
txtInpWC4 = Entry(root, textvariable=FourthtxtInpWC, font=('arial',10,'bold'),bd=1)
txtInpWC4.grid(row=0,column=4,padx=10,pady=10)
txtInpWC5 = Entry(root, textvariable=FifthtxtInpWC, font=('arial',10,'bold'),bd=1)
txtInpWC5.grid(row=0,column=5,padx=10,pady=10)
submit_InpWC = Button(root,text="Submit Input Weight Of Criteria", font=('arial',10,'bold'),bd=1,command=submit_txtInpWC)
submit_InpWC.grid(row=2,column=0)


#Creating the labels for each "DEFENDER & CHALLENGER" column for easy understanding and packing it to the root window
lblcol1 = Label(root, text="LIFE SPAN", font=('arial',10,'bold'),bd=12)
lblcol1.grid(row=3,column=1,padx=0,pady=0)
lblcol2 = Label(root, text="PRICE", font=('arial',10,'bold'),bd=12)
lblcol2.grid(row=3,column=2,padx=0,pady=0)
lblcol3 = Label(root, text="MAINTENANCE COST", font=('arial',10,'bold'),bd=12)
lblcol3.grid(row=3,column=3,padx=0,pady=0)
lblcol4 = Label(root, text="PRODUCTION RATE", font=('arial',10,'bold'),bd=12)
lblcol4.grid(row=3,column=4,padx=0,pady=0)
lblcol5 = Label(root, text="SALVAGE VALUE", font=('arial',10,'bold'),bd=12)
lblcol5.grid(row=3,column=5,padx=0,pady=0)
        
        
#Creating the entry boxes for the "DEFENDER" values and packing it to the root window        
lblDefend = Label(root, text="DEFENDER", font=('arial',10,'bold'),bd=12)
lblDefend.grid(row=4,column=0,padx=20,pady=20)
txtDefend1 = Entry(root, textvariable=FirsttxtDef, font=('arial',10,'bold'),bd=1)
txtDefend1.grid(row=4,column=1,padx=10,pady=10)
txtDefend2 = Entry(root, textvariable=SecondtxtDef, font=('arial',10,'bold'),bd=1)
txtDefend2.grid(row=4,column=2,padx=10,pady=10)
txtDefend3 = Entry(root, textvariable=ThirdtxtDef, font=('arial',10,'bold'),bd=1)
txtDefend3.grid(row=4,column=3,padx=10,pady=10)
txtDefend4 = Entry(root, textvariable=FourthtxtDef, font=('arial',10,'bold'),bd=1)
txtDefend4.grid(row=4,column=4,padx=10,pady=10)
txtDefend5 = Entry(root, textvariable=FifthtxtDef, font=('arial',10,'bold'),bd=1)
txtDefend5.grid(row=4,column=5,padx=10,pady=10)


#Creating the entry boxes for the "CHALLENGER" values and submit button and packing it to the root window
lblChallenge = Label(root, text="CHALLENGER", font=('arial',10,'bold'),bd=12)
lblChallenge.grid(row=8,column=0,padx=10,pady=10)
txtChallenge1 = Entry(root, textvariable=FirsttxtChalng, font=('arial',10,'bold'),bd=1)
txtChallenge1.grid(row=8,column=1,padx=10,pady=10)
txtChallenge2 = Entry(root, textvariable=SecondtxtChalng, font=('arial',10,'bold'),bd=1)
txtChallenge2.grid(row=8,column=2,padx=10,pady=10)
txtChallenge3 = Entry(root, textvariable=ThirdtxtChalng, font=('arial',10,'bold'),bd=1)
txtChallenge3.grid(row=8,column=3,padx=10,pady=10)
txtChallenge4 = Entry(root, textvariable=FourthtxtChalng, font=('arial',10,'bold'),bd=1)
txtChallenge4.grid(row=8,column=4,padx=10,pady=10)
txtChallenge5 = Entry(root, textvariable=FifthtxtChalng, font=('arial',10,'bold'),bd=1)
txtChallenge5.grid(row=8,column=5,padx=10,pady=10)
submit_challenge = Button(root,text="Submit",font=('arial',10,'bold'),bd=1,command=submit_txtChalng)
submit_challenge.grid(row=9,column=0)


#Creating the entry boxes for the "NORMALIZED" output and submit button and packing it to the root window
normalisee = Button(root, text="Normalise",font=('arial',10,'bold'),bd=1,command=lambda:normalise_x())
normalisee.grid(row=25,column=0,padx=10,pady=10)
normal1 = Entry(root,textvariable=Norm1, font=('arial',10,'bold'),bd=1)
normal1.grid(row=24,column=1,padx=10,pady=10)
normal2 = Entry(root,textvariable=Norm2, font=('arial',10,'bold'),bd=1)
normal2.grid(row=24,column=2,padx=10,pady=10)
normal3 = Entry(root,textvariable=Norm3, font=('arial',10,'bold'),bd=1)
normal3.grid(row=24,column=3,padx=10,pady=10)
normal4 = Entry(root,textvariable=Norm4, font=('arial',10,'bold'),bd=1)
normal4.grid(row=24,column=4,padx=10,pady=10)
normal5 = Entry(root,textvariable=Norm5, font=('arial',10,'bold'),bd=1)
normal5.grid(row=24,column=5,padx=10,pady=10)
normal6 = Entry(root,textvariable=Norm6, font=('arial',10,'bold'),bd=1)
normal6.grid(row=25,column=1,padx=10,pady=10)
normal7 = Entry(root,textvariable=Norm7, font=('arial',10,'bold'),bd=1)
normal7.grid(row=25,column=2,padx=10,pady=10)
normal8 = Entry(root,textvariable=Norm8, font=('arial',10,'bold'),bd=1)
normal8.grid(row=25,column=3,padx=10,pady=10)
normal9 = Entry(root,textvariable=Norm9, font=('arial',10,'bold'),bd=1)
normal9.grid(row=25,column=4,padx=10,pady=10)
normal10 = Entry(root,textvariable=Norm10, font=('arial',10,'bold'),bd=1)
normal10.grid(row=25,column=5,padx=10,pady=10)


#Creating the entry boxes for the "SCORE" output and score button and packing it to the root window
score = Button(root,text='Score',font=('arial',10,'bold'),bd=1,command=lambda:score_x())
score.grid(row=34,column=0,padx=10,pady=10)
lblv1 = Label(root,text='DEFENDER', font=('arial',10,'bold'),bd=12)
lblv1.grid(row=33,column=1,padx=10,pady=10)
txtv1 = Entry(root,textvariable=VONE, font=('arial',10,'bold'),bd=1)
txtv1.grid(row=33,column=2,padx=10,pady=10)
lblv2 = Label(root,text='CHALLENGER', font=('arial',10,'bold'),bd=12)
lblv2.grid(row=34,column=1,padx=10,pady=10)
txtv2 = Entry(root,textvariable=VTWO, font=('arial',10,'bold'),bd=1)
txtv2.grid(row=34,column=2,padx=10,pady=10)


#Creating the RESET button and packing it to the root window
reset_btn = Button(root,text='RESET',font=('arial',10,'bold'),bd=1,command=lambda:reset_x())
reset_btn.grid(row=34,column=12,padx=10,pady=10)


if __name__ == '__main__':
    root.mainloop()
    
