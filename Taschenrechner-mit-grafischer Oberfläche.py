#Zu diesem Thema finde man viele Hilfestellungen online. Am besten arbeitet ihr mit der tkinter Doku, um auch zu verstehen, was ihr da
#macht! 


#Hier werden das Modul und die Fonts importiert
import tkinter as tk
from tkinter import font
#Hier wird das fenster definiert
root = tk.Tk()
root.geometry("500x500")
label1=tk. Label(root, text="label1", bg="black")

#Hier wird der/die/das Font definiert
font_cool = font.Font(size=20, family="Terminal")
#Hier werden die Befehle und funktionen definiert
def addChar(char):
 eingabe.insert(len(eingabe.get()), char)

def terminate(): 
 eingabe.delete(0,len(eingabe.get()) )

def show_result():
    result= eval(eingabe.get())
    eingabe.delete(0, tk.END)
    eingabe.insert(0, str(result))


#Hier wird das Eingabefenster erstellt
eingabe = tk.Entry(root, font=font_cool, borderwidth=25)
eingabe.grid(row=0, column=0, columnspan=4)

#Hier werden die Buttons definiert
button1 = tk.Button(root, text="1", font=font_cool, command=lambda: addChar('1'))
button2 = tk.Button(root, text="2", font=font_cool, command=lambda: addChar('2'))
button3=  tk.Button(root, text="3", font=font_cool, command=lambda: addChar('3'))
button4=  tk.Button(root, text="4", font=font_cool, command=lambda: addChar('4'))
button5=  tk.Button(root, text="5", font=font_cool, command=lambda: addChar('5'))
button6=  tk.Button(root, text="6", font=font_cool, command=lambda: addChar('6'))
button7=  tk.Button(root, text="7", font=font_cool, command=lambda: addChar('7'))
button8=  tk.Button(root, text="8", font=font_cool, command=lambda: addChar('8'))

button9=  tk.Button(root, text="9", font=font_cool, command=lambda: addChar('9'))
button0=  tk.Button(root, text="0", font=font_cool, command=lambda: addChar('0'))

button_plus = tk.Button(root, text="+", font=font_cool, command=lambda: addChar('+'))
button_minus = tk.Button(root, text="-", font=font_cool, command=lambda: addChar('-'))
button_geteilt = tk.Button(root, text="/", font=font_cool, command=lambda: addChar('/'))
button_mal = tk.Button(root, text="*", font=font_cool, command=lambda: addChar('*'))
button_ist_gleich = tk.Button(root, text="=", font=font_cool, command=show_result)
button_komma = tk.Button (root, text=".", font=font_cool, command=lambda: addChar('.'))
button_clear = tk.Button(root, text="clear", font=font_cool, command=terminate)

#Hier werden die Buttons in das oben erstellte Fenster "eingebaut"
button7.grid(row=1, column=0, sticky="nswe")
button8.grid(row=1, column=1, sticky="nswe")
button9.grid(row=1, column=2, sticky="nswe")
button_clear.grid(row=1, column=3, sticky="nswe")
button4.grid(row=2, column=0, sticky="nswe")
button5.grid(row=2, column=1, sticky="nswe")
button6.grid(row=2, column=2, sticky="nswe")
button_minus.grid(row=2, column=3, sticky="nswe")
button1.grid(row=3, column=0, sticky="nswe")
button2.grid(row=3, column=1, sticky="nswe")
button3.grid(row=3, column=2, sticky="nswe")
button_plus.grid(row=3, column=3, sticky="nswe")
button_mal.grid(row=4, column=0, sticky="nswe")
button0.grid(row=4, column=1, sticky="nswe")
button_geteilt.grid(row=4, column=2, sticky="nswe")
button_ist_gleich.grid(row=4, column=3, sticky="nswe")
button_komma.grid (row=5, column=1, sticky="nswe")

for column in range (5):
  root.columnconfigure(column,weight=1)


for row in range (4):
  root.rowconfigure(row,weight=1 )


root.mainloop()