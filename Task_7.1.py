from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO

Allowed_tags = ['sleep', 'jump', 'fight', 'black', 'white', 'siamese', 'cute']


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


def open_new_window():
    tag = tag_combobox.get()
    url_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title('Новый котик')
        new_window.geometry('600x480')
        lab = Label(new_window, image=img)
        lab.pack()
        lab.image = img


def rand_cat():
    url = 'https://cataas.com/cat'
    img = load_image(url)

    if img:
        new_window = Toplevel()
        new_window.title('Случайный котик')
        new_window.geometry('600x480')
        lab = Label(new_window, image=img)
        lab.pack()
        lab.image = img

def exit():
    window.destroy()


window = Tk()
window.title('Котики')
window.geometry('400x300')

new_cat = Button(text='Случайный котик', command=rand_cat, pady=10)
new_cat.pack()

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить новое фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit)

tag_lab = Label(text='Выбери тег', pady=10)
tag_lab.pack()

tag_combobox = ttk.Combobox(values=Allowed_tags)
tag_combobox.pack()

load_but = Button(text='Загрузить по тегу', command=open_new_window, pady=10)
load_but.pack()

window.mainloop()
