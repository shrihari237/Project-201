from tkinter import *

window = Tk()
window.configure(width = 800 , height = 600)
window.title("Simple Interest Calculator")

def calculate_interest():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    i = (p*r*t)/100

    interest = round(i,2)
    Showlabel.destroy()

    
    message = Label(result_frame,text="Interest on Rs."+str(p)+"at rate of interest"+str(r)+"N for"+str(t)+"years is Rs."+str(interest),bg="grey",font=("Calibri",12),width=55)
    message.place(x=20,y=40)
    message.pack()

label = Label(window,font="Helvetica 14 bold",text="Simple Interest Calculator")
label.place(x=20, y=20)

principal_label = Label(window,font="Helvetica 14 bold",text="Enter the principal")
principal_label.place(x=20, y=92) 

rate_label = Label(window,font="Helvetica 14 bold",text="Enter the Rate")
rate_label.place(x=20, y=140)

time_label = Label(window,font="Helvetica 14 bold",text="Enter the Time")
time_label.place(x=20, y=185)


principal_entry = Entry(window,text="",font="Helvetica 12 bold")
principal_entry.place(x=200,y=92)

rate_entry = Entry(window,text="",font="Helvetica 12 bold")
rate_entry.place(x=200,y=142)

time_entry = Entry(window,text="",font="Helvetica 12 bold")
time_entry.place(x=200,y=187)

button = Button(window,text="Calulate",font="Helvetica 14 bold",command=calculate_interest)
button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result",bg="grey",font=("Calibri",12))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=300)

Showlabel = Label(result_frame,text="Your result will be displayed here",bg="grey",font=("Calibri",12),width=55)
Showlabel.place(x=20,y=20)
Showlabel.pack()





window.mainloop()

