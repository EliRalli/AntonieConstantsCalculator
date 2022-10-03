# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:03:46 2020

@author: bofoi
"""

import tkinter as tk
import pandas as pd
import numpy as np

dfData=pd.read_excel('C:/Users/bofoi/PythonScript/Antoine_Constants_1.xlsx',Sheet_Name= 'Sheet 1')


dfChemName=input('Enter a Chemical  ')
comp = dfData.where(dfData['Chemical'] == dfChemName).dropna()
Chemical=comp['Chemical']
A=comp['A'].to_numpy()
B=comp['B'].to_numpy()
C=comp['C'].to_numpy()
Tmin=comp['Tmin'].to_numpy()
Tmax=comp['Tmax'].to_numpy()

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Calculate Saturation Pressure')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type your Temperature in Celcius:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 

canvas1.create_window(200, 140, window=entry1)
def getPsat ():
    
    x1 = entry1.get()
    
    label3 = tk.Label(root, text= 'The Saturation of given Temeprature  ' + x1 + ' is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    x2=np.exp((A-(B/(float(x1)+C))))
    label4 = tk.Label(root, text= float(x2),font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='Get the Saturation Pressure', command=getPsat, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()