import tkinter as tk
import os

m = tk.Tk()
m.title('Runner Tracker')
m.geometry('600x150')


file_name = input("Enter filename: ")

def open_chart():
    os.startfile("conversion_chart.png")
    
def save_tracker():
    distance_track = distance.get()
    date_track = date.get()
##    print(distance_track, date_track, sep=" -- ")
    file = open(file_name + ".txt", "a")
    file.write("Date: ")
    file.write(date_track)
    file.write("   ==>>   ")
    file.write("Distance: ")
    file.write(distance_track)
    file.write("\n")
    print("SAVED")
    file.close()
    

def view_tracker():
    os.startfile(file_name + ".txt")
    print("OPEND")


distance_txt = tk.Label(text='How far have you ran today?(## unit)').grid(row=1)
date_txt = tk.Label(text='Enter the date(DD/MM/YYYY)').grid(row=2)

distance = tk.StringVar()
date = tk.StringVar()

distance_ent = tk.Entry(textvariable=distance)
date_ent = tk.Entry(textvariable=date)

distance_ent.grid(row=1, column=2)
date_ent.grid(row=2, column=2)


save_btn = tk.Button(m, text='Submit', width=15, bg="yellow", height=2,
                command=save_tracker)
save_btn.grid(row=4, column=1)


view_btn = tk.Button(m, text='View track', width=15, bg="green", height=2,
                command=view_tracker)
view_btn.grid(row=4, column=2)

chart_btn = tk.Button(m, text='Conversion Chart', width=15, bg="blue", height=2,
                      command=open_chart)
chart_btn.grid(row=4, column=3)

m.mainloop()



    
