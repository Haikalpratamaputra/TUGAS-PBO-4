# main.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W
import fungsi

def hitung_luas_selimut():
    r = float(txtjarijari.get())
    t = float(txttinggi.get())
    
    LS = fungsi.hitung_luas_selimut(r,t,phi=3.14)
    txtluas_selimut.delete(0,END)
    txtluas_selimut.insert(END,LS)
    
def hitung_luas_permukaan():
    r = float(txtjarijari.get())
    t = float(txttinggi.get())

    LP = fungsi.hitung_luas_permukaan(r,t,phi=3.14)
    txtluas_permukaan.delete(0,END)
    txtluas_permukaan.insert(END,LP)

def hitung_volume():
    r = float(txtjarijari.get())
    t = float(txttinggi.get())

    v = fungsi.hitung_volume(r,t,phi=3.14)
    txtvolume.delete(0,END)
    txtvolume.insert(END,v)

def hitung():
    hitung_luas_selimut()
    hitung_luas_permukaan()
    hitung_volume()

# Create tkinter Object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Volume Silinder (Tabung)")

# Windows
frame = Frame(app)
frame.pack(padx=20,pady=20)

# Label Jari - Jari Lingkaran Tabung
jarijari = Label(frame,text="Jari - Jari Lingkaran Tabung:")
jarijari.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox Jari - Jari Lingkaran Tabung
txtjarijari = Entry(frame)
txtjarijari.grid(row=0,column=1)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=1,column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Luas Selimut
luas_selimut = Label(frame, text="Luas Selimut:")
luas_selimut.grid(row=3, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Selimut
txtluas_selimut = Entry(frame)
txtluas_selimut.grid(row=3, column=1)

# Output Luas Permukaan
luas_permukaan = Label(frame, text="Luas Permukaan:")
luas_permukaan.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Permukaan
txtluas_permukaan = Entry(frame)
txtluas_permukaan.grid(row=4, column=1)

# Output Volume
volume = Label(frame, text="Volume:")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)
# Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=5, column=1)

app.mainloop()