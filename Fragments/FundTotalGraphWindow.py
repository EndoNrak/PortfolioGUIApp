import matplotlib.pyplot as plt
import tkinter as tk


class FundTotalGraphWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=400, height=300, bg="blue")
        self.pack(side="right")
        self.setup()
        self.master = master

    def setup(self):
        title_frame = tk.Label(self, text="時価総額", font=("ＭＳ ゴシック", 15, "bold"))
        title_frame.place(x=0.5, y=0.1)

