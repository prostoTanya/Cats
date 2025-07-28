from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO


def load_image():
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None


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
