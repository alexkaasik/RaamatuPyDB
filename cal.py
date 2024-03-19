from tkinter import *
import calendar
cal = Tk()

w = Spinbox(cal, from_=0,to=9999)
w.pack()

ym=calendar.monthrange(2024,2)[1]
print(ym)

cal.mainloop()
