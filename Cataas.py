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


def exit():
    window.destroy()


window = Tk()
window.title('Котики')
window.geometry('600x480')

lab = Label()
lab.pack()

# upd_but = Button(text='Новый котик', command=set_img)
# upd_but.pack()

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить новое фото', command=set_img)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit)

url ='https://cataas.com/cat'

set_img()

window.mainloop()
