import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk
# from PIL import ImageResampling 
window= tk.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.title("Welcome")
window.geometry(f"{screen_width}x{screen_height}")

# frame = tk.Frame(window, bg = "white")
# frame.place(x = 0, y = 0, width = screen_width, height = screen_height)

# imageFormWelcome = Image.open("D:\\Python\\python-T2\\Dataset\\image_form\\imgForm.jpg")
# imageFormWelcome = imageFormWelcome.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

# imageBackground = ImageTk.PhotoImage(imageFormWelcome)

# imageForm = tk.Label(frame, image = imageBackground)
# imageForm.place(x = 0, y = 0, relwidth=1,relheight=1)