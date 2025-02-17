import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Thông báo", "Bạn đã nhấn nút!")

root = tk.Tk()
root.title("Cửa sổ đơn giản")      
root.geometry("400x300")           

label = tk.Label(root, text="Chào mừng đến với cửa sổ đơn giản", font=("Arial", 14))
label.pack(pady=20)                
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

button = tk.Button(root, text="Nhấn vào đây", font=("Arial", 12), command=on_button_click)
button.pack(pady=10)

root.mainloop()