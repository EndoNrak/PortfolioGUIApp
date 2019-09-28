import tkinter as tk
from PIL import Image, ImageTk
import os.path


class TodayWindow(tk.Frame):
    def __init__(self, title, today_value, dif_value, master=None):
        super().__init__(master, height=100, width=100)
        self.propagate(False)
        self.frame_title = title
        self.today_value = today_value
        self.dif_value = dif_value
        self.setup_window()

    # 前日比で+なら青、-なら赤、0なら灰色
    def dif_color(self):
        if self.dif_value > 0:
            return "blue"
        elif self.dif_value < 0:
            return "red"
        else:
            return "gray"

    def title_image(self):
        cur_dir = os.getcwd()
        dir_name_japan = os.path.join(cur_dir, "image\\japan.png")
        dir_name_us = os.path.join(cur_dir, "image\\アメリカ国旗.jpg")
        dir_name_usdjpy = os.path.join(cur_dir, "image\\USDJPY.png")

        images = {"日経平均": dir_name_japan, "TOPIX": dir_name_japan, "NYダウ": dir_name_us,
                  "sp500": dir_name_us, "USD/JPY": dir_name_usdjpy}
        if self.frame_title in images:
            image_name = images[self.frame_title]
        img = Image.open(image_name)
        resized_img = img.resize((20, 13), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        return photo_img

    def setup_window(self):
        title_frame = tk.Frame(self)
        frame_title = tk.Label(title_frame, text=self.frame_title, fg="gray", font=("Arial", 11))
        frame_title_image = tk.Canvas(title_frame, height=15, width=17)
        frame_title_image.photo = self.title_image()
        frame_title_image.create_image(0, 1, image=frame_title_image.photo, anchor="nw")
        frame_title.pack(side="left")
        frame_title_image.pack(side="left")
        title_frame.place(relx=0.05, rely=0.05)
        today_value_column = tk.Label(self, text=self.today_value, font=("Arial", 18))
        today_value_column.place(anchor="c", relx=0.5, rely=0.5)
        frame_dif_value = tk.Label(self, text="{:+}".format(self.dif_value), font=("Arial", 11)
                                   , bg=self.dif_color(), fg="white")
        frame_dif_value.place(anchor="se", relx=0.95, rely=0.95)
