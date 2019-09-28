import tkinter as tk
from Functions.ConnectDB import DB
from Model.FundDetails import FundDetails


class ShowFundDetailsWindow(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master, width=400)
        self.pack(side="left")
        self.table_canvas = tk.Canvas(self)
        self.table_canvas.pack(side="left")
        self.set_y_scrollbar(self)
        self.show_fund_details_table(self.table_canvas)

    def set_y_scrollbar(self, master=None):
        scroll_y = tk.Scrollbar(master, command=self.table_canvas.yview)
        scroll_y.pack(side="left", fill="y")
        # self.table_canvas.yview_scroll()
        self.table_canvas.configure(yscrollcommand=scroll_y.set)
        self.table_canvas.configure(scrollregion=(0, 0, 300, 1000))

    @staticmethod
    def show_fund_details_table(master=None):
            today_data_list = DB().get_today_prices()
            yesterday_data_list = DB().get_second_latest_prices()
            for i in today_data_list:
                today_data = i
                yesterday_data = yesterday_data_list[today_data_list.index(i)]
                input_data = FundDetails(today_data, yesterday_data).get_fund_detail_data()
                fund_column = FundDetailsFrame(input_data, master)
                fund_column.pack(side="top")


class FundDetailsFrame(tk.Frame):
    def __init__(self, data, master=None):
        super().__init__(master, relief="solid", height=80, width=380)
        self.propagate(False)
        self.fund_name = data["name"]
        self.fund_code = data["code"]
        self.today_price = data["today_price"]
        self.diff = data["price_diff"]
        self.count = data["count"]
        self.purchase_price = data["purchase_price"]
        self.total = self.today_price * self.count
        self.total_benefit = data["benefit"]
        self.setup()

    @staticmethod
    def dif_color(value):
        if value > 0:
            return "blue"
        elif value < 0:
            return "red"
        else:
            return "gray"

    def setup(self):
        frame_title = tk.Label(self, text=self.fund_name, fg="black", font=("ＭＳ ゴシック", 11, "bold"))
        frame_title.place(relx=0.05, rely=0.08)
        total_price_label = tk.Label(self, text="時価", fg="#a0a0a0", font=("ＭＳ ゴシック", 9))
        total_price_label.place(anchor="w", relx=0.4, rely=0.5)
        total_price = tk.Label(self, text="{:,}".format(int(self.total)), font=("Arial", 13))
        total_price.place(anchor="e", relx=0.7, rely=0.5)

        count_label = tk.Label(self, text="保有数", fg="#a0a0a0", font=("ＭＳ ゴシック", 9))
        count_label.place(anchor="w", relx=0.4, rely=0.8)
        count_column = tk.Label(self, text=self.count, font=("Arial", 11))
        count_column.place(anchor="e", relx=0.7, rely=0.8)

        total_benefit = tk.Label(self, text="損益", fg="#a0a0a0", font=("ＭＳ ゴシック", 9))
        total_benefit.place(anchor="e", relx=0.85, rely=0.5)

        total_dif_previous_day = tk.Label(self, text="前日比", fg="#a0a0a0", font=("ＭＳ ゴシック", 9))
        total_dif_previous_day.place(anchor="e", relx=0.85, rely=0.8)

        today_value_column = tk.Label(self, text="{:,}".format(int(self.today_price)), font=("Arial", 20))
        today_value_column.place(anchor="w", relx=0.1, rely=0.7)

        frame_dif_benefit = tk.Label(self, text="{:+}".format(int(self.total_benefit)), font=("Arial", 13),
                                     fg=self.dif_color(self.total_benefit))
        frame_dif_benefit.place(anchor="e", relx=0.99, rely=0.5)
        frame_dif_value = tk.Label(self, text="{:+}".format(int(self.diff)), font=("Arial", 13),
                                   fg=self.dif_color(self.diff))
        frame_dif_value.place(anchor="e", relx=0.99, rely=0.8)
