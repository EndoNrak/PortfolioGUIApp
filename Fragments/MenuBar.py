import tkinter as tk


def back_to_mainmenu():
    print("メインメニューに戻ったつもりになってください")


def show_help():
    print("ヘルプを見た気分になってください")


def exit():
    print("exitした気持ちになってください")


class MenuBar(tk.Menu):
    def __init__(self, master=None):
        super().__init__(master)
        # self.root = master
        self.setup_menu()

    def setup_menu(self):
        file_menu = tk.Menu(self)
        file_menu.add_command(label='メインメニュー', command=back_to_mainmenu)
        file_menu.add_separator()
        file_menu.add_command(label="exit", command=exit)
        help_menu = tk.Menu(self)
        help_menu.add_command(label="ヘルプ", command=show_help)

        self.add_cascade(label='File', menu=file_menu)
        self.add_cascade(label="Help", menu=help_menu)
