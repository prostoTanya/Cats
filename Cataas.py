from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

from pygame.examples.aliens import load_image

window = Tk()
window.title('Котики')
window.geometry('600x480')

lab = Label()
lab.pack()

url ='https://cataas.com/cat'
img = load_image(url)

if img:
    lab.config(image=img)
    lab.image = img

window.mainloop()
