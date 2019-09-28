import tkinter as tk
from Fragments.MenuBar import MenuBar
from Fragments.TodayWindow import TodayWindow
from Fragments.TodayPortfolio import TodayPortfolioFrame
from Functions.CulculateFunctions import today_calculation
from Fragments.FundDetailFrame import ShowFundDetailsWindow
from Fragments.FundTotalGraphWindow import FundTotalGraphWindow


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frame2 = None
        self.fund_list_window = None
        self.total_graph_window = None
        self.is_detail_open = False
        self.is_total_graph_open = False
        self.setup(master)

    def show_fund_details(self):
        self.fund_list_window = ShowFundDetailsWindow(master=self.frame2)
        self.is_detail_open = True

    def close_fund_details(self):
        self.fund_list_window.destroy()
        self.is_detail_open = False

    def switch_func_details(self, event):
        if not self.is_detail_open:
            self.show_fund_details()
        else:
            self.close_fund_details()

    def show_total_graph(self):
        self.total_graph_window = FundTotalGraphWindow(master=self.frame2)
        self.is_total_graph_open = True

    def close_total_graph(self):
        self.total_graph_window.destroy()
        self.is_total_graph_open = False

    def switch_func_total_graph(self, event):
        if not self.is_total_graph_open:
            self.show_total_graph()
        else:
            self.close_total_graph()

    def setup(self, master):
        master.title(u"メインメニュー")
        master.geometry("800x600")

        menu_bar = MenuBar(master)
        master.configure(menu=menu_bar)

        frame1 = tk.Frame(master, width=800, height=300, bg="#4348c1")
        self.frame2 = tk.Frame(master, width=800, height=300, background='white')
        self.frame2.propagate(False)

        today_frame1 = TodayWindow("日経平均", "20,000", +199.69, frame1)
        today_frame1.place(relx=0.05, rely=0.05)
        today_frame2 = TodayWindow("NYダウ", "30,000", 0, frame1)
        today_frame2.place(relx=0.2, rely=0.05)
        today_frame3 = TodayWindow("TOPIX", "1,500", -14.2, frame1)
        today_frame3.place(relx=0.35, rely=0.05)
        today_frame4 = TodayWindow("sp500", "1,500", -12, frame1)
        today_frame4.place(relx=0.5, rely=0.05)
        today_frame5 = TodayWindow("USD/JPY", 107.5, -0.4, frame1)
        today_frame5.place(relx=0.65, rely=0.05)

        today = today_calculation()
        today_portfolio1 = TodayPortfolioFrame("投資信託", today[0], today[1], today[2], self.switch_func_details,
                                               self.switch_func_total_graph, frame1)
        today_portfolio1.place(relx=0.05, rely=0.45)
        frame1.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.frame2.grid(row=1, column=0)


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
