import tkinter as tk
from tkinter import Tk,Frame,Label,Entry,Button,END, W
from Fungsi import hitung_luas, hitung_volume

# Create tkinter object
app = Tk()

# Tambahkan judul
app.title("kalkulator luas dan volume Balok")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Panjang
panjang= Label(frame, text="panjang:")
panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox Panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=0, column=1)

# Label Lebar 
lebar= Label(frame, text="lebar:")
lebar.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox Lebar
txtlebar = Entry(frame)
txtlebar.grid(row=1, column=1)

# Label Tinggi 
tinggi= Label(frame, text="tinggi:")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi   .grid(row=2, column=1)

# Label Luas 
luas= Label(frame, text="luas:")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Luas
txtluas = Entry(frame)
txtluas.grid(row=3, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Label Volume
volume= Label(frame, text="volume:")
volume.grid(row=8, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ")
luas.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="volume: ")
volume.grid(row=8, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=8, column=1, sticky=W, padx=5, pady=5)

app.mainloop()

