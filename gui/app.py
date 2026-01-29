import tkinter as tk
from tkinter import ttk
from gui.tab_clean import TabClean
from gui.tab_convert import TabConvert
from gui.tab_crawl import TabCrawl
from gui.tab_train import TabTrain
from gui.tab_predict import TabPredict
from gui.tab_visualize import TabVisualize
from gui.tab_word_cloud import TabWordCloud
# import tkinter.font as TkFont

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Công cụ gom cụm văn bản')

        # default_font = TkFont.nametofont('TkDefaultFont')
        # default_font.configure(size=9)
        # self.option_add('*Font', default_font)

        # Tao notebook chua cac tab
        self.notebook = ttk.Notebook(self)

        # Tao các tab con
        self.tab_crawl = TabCrawl(self.notebook)
        self.tab_convert = TabConvert(self.notebook)
        self.tab_clean = TabClean(self.notebook)
        self.tab_train = TabTrain(self.notebook)
        self.tab_predict = TabPredict(self.notebook)
        self.tab_visualize = TabVisualize(self.notebook)
        self.tab_word_cloud = TabWordCloud(self.notebook)

        # Gắn các tab con vào notebook
        self.notebook.add(self.tab_crawl, text='Cào ngữ liệu')
        self.notebook.add(self.tab_convert, text='Chuyển đổi ngữ liệu')
        self.notebook.add(self.tab_clean, text='Làm sạch ngữ liệu')
        self.notebook.add(self.tab_train, text='Huấn luyện')
        self.notebook.add(self.tab_predict, text='Gom cụm')
        self.notebook.add(self.tab_visualize, text='Trực quan hóa')
        self.notebook.add(self.tab_word_cloud, text='Word cloud')

        self.notebook.pack(expand=1, fill='both')