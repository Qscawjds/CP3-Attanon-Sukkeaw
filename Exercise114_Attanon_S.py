from currency_converter import CurrencyConverter
from datetime import *
from tkinter import *

c = CurrencyConverter(fallback_on_missing_rate=True)
main_window = Tk()

def convert_money(event):
    value_conversion = c.convert(textbox_amount.get(), textbox_currency_1.get(), textbox_currency_2.get(), date=date(int(textbox_years.get()),int(textbox_month.get()),int(textbox_date.get())))
    print(value_conversion)
    result.configure(text=value_conversion)
    
    
label_amount = Label(main_window,text = "Amount")
label_amount.grid(row = 0,column = 0)
textbox_amount = Entry(main_window)
textbox_amount.grid(row = 0,column = 1)

label_currency_1 = Label(main_window,text = "Type Of Currency1")
label_currency_1.grid(row = 1,column = 0)
textbox_currency_1 = Entry(main_window)
textbox_currency_1.grid(row = 1,column = 1)

label_currency_2 = Label(main_window,text = "Type Of Currency2")
label_currency_2.grid(row = 2,column = 0)
textbox_currency_2 = Entry(main_window)
textbox_currency_2.grid(row = 2,column = 1)

label_datetime = Label(main_window,text = "Date Of Time")
label_datetime.grid(row = 3,column = 0)

label_years = Label(main_window,text = "Years")
label_years.grid(row = 4,column = 0)
textbox_years = Entry(main_window)
textbox_years.grid(row = 4,column = 1)

label_month = Label(main_window,text = "Month")
label_month.grid(row = 5,column = 0)
textbox_month = Entry(main_window)
textbox_month.grid(row = 5,column = 1)

label_date = Label(main_window,text = "Date")
label_date.grid(row = 6,column = 0)
textbox_date = Entry(main_window)
textbox_date.grid(row = 6,column = 1)

button = Button(main_window,text = "Convert")
button.bind("<Button-1>",convert_money)
button.grid(row = 7,column = 0)

result = Label(main_window,text = "Result")
result.grid(row = 7,column = 1)

main_window.mainloop()