import requests
import tkinter as tk
from PIL import Image, ImageTk
import io


response = requests.get("https://reqres.in/api/users/")
user_data = response.json()

root = tk.Tk()
root.title("User Information")

def load_image(url):
    response = requests.get(url)
    image_data = Image.open(io.BytesIO(response.content))
    return ImageTk.PhotoImage(image_data)


for index, person in enumerate(user_data["data"]):
    Email = person.get('email')
    Name = person.get('first_name')
    picture = person.get('avatar')


    img = load_image(picture)


    user_frame = tk.Frame(root)
    user_frame.grid(row=index // 3, column=index % 3, padx=10, pady=10)


    img_label = tk.Label(user_frame, image=img)
    img_label.image = img
    img_label.pack()


    info_label = tk.Label(user_frame, text=f"{Name}\n{Email}")
    info_label.pack()

root.mainloop()

