from tkinter import *

main_window = Tk()

def arithmetic_sequence(event):
    #an คือ พจน์ทั่วไปของลำดับนั้น
    an = int(entry_a1.get()) + (int(entry_n.get())-1) * int(entry_d.get())
    label_result_arithmethic.configure(text = an)

def geometric_sequence(event):
    #an คือ พจน์ทั่วไปของลำดับนั้น
    an_2 = int(entry_a1_2.get()) * (int(entry_r.get()) ** (int(entry_n_2.get())-1))
    label_result_geometric.configure(text = an_2)
    
label_topic = Label(main_window, text="โปรแกรมคำนวณลำดับเลขและเรขาคณิต")
label_topic.grid(row=0, column=0, columnspan=2) 

label_arithmethic = Label(main_window, text="ลำดับเลขคณิต") 
label_arithmethic.grid(row=1, column=0, columnspan=2) 


label_a1 = Label(main_window, text="a1") #a1 คือ พจน์แรกหรือเลขตัวแรกของลำดับนั้น
label_a1.grid(row=2, column=0)
entry_a1 = Entry(main_window)
entry_a1.grid(row=2, column=1)

label_d = Label(main_window, text="d") #d คือ ผลต่างร่วมของลำดับเลขคณิต
label_d.grid(row=3, column=0)
entry_d = Entry(main_window)
entry_d.grid(row=3, column=1)

label_n = Label(main_window, text="n") #n คือ จำนวนพจน์ในลำดับนั้นทั้งหมด
label_n.grid(row=4, column=0)
entry_n = Entry(main_window)
entry_n.grid(row=4, column=1)

result_arithmethic = Button(main_window,text = "คำนวณ")
result_arithmethic.bind("<Button-1>",arithmetic_sequence)
result_arithmethic.grid(row = 5,column = 0)

label_result_arithmethic = Label(main_window,text = "ผลลัพท์")
label_result_arithmethic.grid(row = 5,column = 1)

label_geometric = Label(main_window, text="ลำดับเรขาคณิต")
label_geometric.grid(row=6, column=0, columnspan=2) 

label_a1_2 = Label(main_window, text="a1") #a1 คือ พจน์แรกหรือเลขตัวแรกของลำดับนั้น
label_a1_2.grid(row=7, column=0)
entry_a1_2 = Entry(main_window)
entry_a1_2.grid(row=7, column=1)

label_r = Label(main_window, text="r") #r คือ อัตราส่วนร่วมของลำดับเรขาคณิต
label_r.grid(row=8, column=0)
entry_r = Entry(main_window)
entry_r.grid(row=8, column=1)

label_n_2 = Label(main_window, text="n") #n คือ จำนวนพจน์ในลำดับนั้นทั้งหมด
label_n_2.grid(row=9, column=0)
entry_n_2 = Entry(main_window)
entry_n_2.grid(row=9, column=1)

result_geometric = Button(main_window,text = "คำนวณ")
result_geometric.bind("<Button-1>",geometric_sequence)
result_geometric.grid(row = 10,column = 0)

label_result_geometric = Label(main_window,text = "ผลลัพท์")
label_result_geometric.grid(row = 10,column = 1)

main_window.mainloop()