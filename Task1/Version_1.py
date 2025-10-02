import tkinter as tk
import random
import string
import pygame

pygame.mixer.init()

def generar_keygen():
    key_g = []    
    for i in range(3):
        while True:
            key = ''.join([random.choice(string.ascii_uppercase) for _ in range(4)])
            suma = 0
            for caracter in key:
                suma += (ord(caracter) - 64)
            if suma >= 30 and suma <= 35:
                key_g.append(key)
                break
    keygen = ' - '.join(key_g)
    
    txt_keygen.config(state='normal')
    txt_keygen.delete('1.0', tk.END)
    txt_keygen.insert('1.0', keygen)
    txt_keygen.config(state='disabled')


pygame.mixer.music.load("COD3.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)


root = tk.Tk()
root.title("COD III")
root.geometry("640x360")
root.resizable(False, False)

image = tk.PhotoImage(file="background.png")  
bg = tk.Label(root, image=image)
bg.place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(root, text="Keygen Generator COD III", bg='black', fg='white', font=('Arial', 18)).pack(pady=30)
tk.Button(root, text="Generate", bg='gray', fg='black', font=('Arial', 18), command=generar_keygen).pack(pady=80)

txt_keygen = tk.Text(root, bg='black', fg='white', font=('Courier New', 14), width=20, border=0)
txt_keygen.pack()
txt_keygen.insert('1.0', "XXXX - XXXX - XXXX")
txt_keygen.config(state='disabled')

root.mainloop()