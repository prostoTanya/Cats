from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None


def set_img():
    img = load_image(url)

    if img:
        lab.config(image=img)
        lab.image = img


window = Tk()
window.title('Котики')
window.geometry('600x520')

lab = Label()
lab.pack()

upd_but = Button(text='Новый котик', command=set_img)
upd_but.pack()

url ='https://cataas.com/cat'

set_img()

window.mainloop()
