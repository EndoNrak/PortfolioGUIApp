import tkinter as tk


class TodayPortfolioFrame(tk.Frame):
    def __init__(self, title, today_value, total_benefit, total_dif, on_click, on_click_total, master=None):
        super().__init__(master, height=120, width=350)
        self.propagate(False)
        self.frame_title = title
        self.today_value = today_value
        self.total_benefit = total_benefit
        self.total_dif = total_dif
        self.on_click = on_click
        self.on_click_total = on_click_total
        self.setup_window()

    @staticmethod
    def dif_color(value):
        if value > 0:
            return "blue"
        elif value < 0:
            return "red"
        else:
            return "gray"

    def setup_window(self):
        fund_detail_btn = tk.Button(self, height=120, width=350)
        fund_detail_btn.bind("<1>", self.on_click)
        fund_detail_btn.propagate(False)
        fund_detail_btn.pack(side="left")

        total_frame = tk.Frame(self, height=70, width=150)
        total_frame.place(relx=0.05, rely=0.3, anchor="nw")

        total_btn = tk.Button(total_frame, height=3, width=23)
        # total_btn.propagate(False)
        total_btn.pack(fill="both")
        total_btn.bind("<1>", self.on_click_total)

        today_value_column = tk.Label(total_frame, text="{:,}".format(int(self.today_value)), font=("Arial", 20))
        today_value_column.place(anchor="nw", relx=0.1, rely=0.3)

        total_price = tk.Label(total_frame, text="時価総額", fg="#a0a0a0", font=("ＭＳ ゴシック", 11))
        total_price.place(anchor="nw", relx=0, rely=0)

        frame_title = tk.Label(self, text=self.frame_title, fg="black", font=("ＭＳ ゴシック", 12, "bold"))
        frame_title.place(relx=0.05, rely=0.08)

        total_benefit = tk.Label(self, text="損益", fg="#a0a0a0", font=("ＭＳ ゴシック", 11))
        total_benefit.place(anchor="e", relx=0.7, rely=0.4)

        total_dif_previous_day = tk.Label(self, text="前日比", fg="#a0a0a0", font=("ＭＳ ゴシック", 11))
        total_dif_previous_day.place(anchor="e", relx=0.7, rely=0.7)

        frame_dif_benefit = tk.Label(self, text="{:+,}".format(self.total_benefit), font=("Arial", 13),
                                     fg=self.dif_color(self.total_benefit))
        frame_dif_benefit.place(anchor="c", relx=0.8, rely=0.5)
        frame_dif_value = tk.Label(self, text="{:+,}".format(self.total_dif), font=("Arial", 13),
                                   fg=self.dif_color(self.total_dif))
        frame_dif_value.place(anchor="c", relx=0.8, rely=0.8)
