import pandas as pd 
import tkinter as tk 
from tkinter import *
from sklearn.linear_model import LinearRegression
window = Tk()
window.geometry('300x250')
window.title('Data Prediction')

file_name = tk.Entry(window)
file_name.pack()

x = tk.Entry(window)
x.pack()

y = tk.Entry(window)
y.pack()

input = tk.Entry(window)
input.pack()

labelX = tk.Label(window,text='X')
labelX.place(relx=0.25,rely=0.07,anchor='ne')

labelY = tk.Label(window,text='Y')
labelY.place(relx=.25,rely=.14,anchor='ne')

inputLabel = tk.Label(window,text='Input Value')
inputLabel.place(relx=.25,rely=.21,anchor='ne')

file_label = tk.Label(window,text='File Name')
file_label.place(relx=.25,rely=.001,anchor='ne')


def prediction():
    data = pd.read_excel("C:\\users\\HP\\Documents\\Datascience task\\" + file_name.get())

    get_x = x.get()
    get_y = y.get()
    get_input = input.get()

    x0 = data[[get_x]]
    y0 = data[[get_y]]

    lr = LinearRegression()
    lr.fit(x0,y0)

    prediction = lr.predict([[get_input]])
    pred_label = tk.Label(window,text=prediction)
    pred_label.pack()

button = tk.Button(window, text="Perform Prediction",width=15,command=prediction)
button.pack()   

window.mainloop()
