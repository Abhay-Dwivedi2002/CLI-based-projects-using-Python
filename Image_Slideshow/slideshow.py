from itertools import cycle
from PIL import Image,ImageTk
import time
import tkinter as tk

root= tk.Tk()
root.title("Image Slideshow Viewer")


#List of Image Path
image_paths = [
    r"Copy Paste Path of the Images",
    r"Copy Paste Path of the Images",
    r"Copy Paste Path of the Images",
    r"Copy Paste Path of the Images",
    r"Copy Paste Path of the Images",
]


# Resize the images to 480x480
image_size =(480,480)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]


label = tk.Label(root)
label.pack()


slideshow = cycle(photo_images)

def update_image():
    photo_image = next(slideshow)
    label.config(image = photo_image)
    root.after(2000, update_image)   # Schedule next update after 2 sec


def start_slideshow():
    update_image()

play_button = tk.Button(root, text='Play Slideshow', command = start_slideshow)
play_button.pack()

root.mainloop()
