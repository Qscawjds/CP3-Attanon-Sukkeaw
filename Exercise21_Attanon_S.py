from tkinter import *
import math

def leftClickButton(event):
    BMI = (float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    labelResult.configure(text = BMI) 
    if BMI >=30:
        x = "อ้วนมาก"
    elif 25<=BMI<=29.9:
        x = "อ้วน"
    elif 23<=BMI<=24.9:
        x = "น้ำหนักเกินเกณฑ์"
    elif 18.6<=BMI<=22.9:
        x = "น้ำหนักปกติ/เหมาะสม"
    else:
        x = "ผอมเกินไป"
    labelBMI.configure(text = x)
        
        
main = Tk()

labelHeight = Label(main,text ="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)

textBoxHeight = Entry(main)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(main,text ="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)

textBoxWeight = Entry(main)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(main,text ="คำนวณ")
calculateButton.bind("<Button-1>",leftClickButton)
calculateButton.grid(row=2,column=0)

labelResult = Label(main,text ="ผลลัพท์")
labelResult.grid(row=2,column=1)

labelBMI = Label(main,text ="เกณฑ์ดัชนีมวลกาย")
labelBMI.grid(row=4,column=1)
main.mainloop()