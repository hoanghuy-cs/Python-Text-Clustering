import json
from tkinter import messagebox, ttk
import tkinter as tk
from core.common import WORD_CLOUD_DEFAULT_PARAMS
from core.word_cloud import draw_word_cloud
from gui.common import choose_file

class TabWordCloud(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.master = master

        # Widget chon file van ban
        ttk.Label(self, text='File cụm:').grid(column=0, row=0, sticky='e')
        self.ent_doc = ttk.Entry(self)
        self.ent_doc.grid(column=1, row=0, sticky='we', padx=10, pady=5)
        self.btn_doc = ttk.Button(self, text='Chọn', command=lambda: choose_file(self.ent_doc))
        self.btn_doc.grid(column=2, row=0)

        # Widget chon file van ban
        ttk.Label(self, text='File stopwords:').grid(column=0, row=1, sticky='e')
        self.ent_stopwords = ttk.Entry(self)
        self.ent_stopwords.grid(column=1, row=1, sticky='we', padx=10, pady=5)
        self.btn_stopwords = ttk.Button(self, text='Chọn', command=lambda: choose_file(self.ent_stopwords))
        self.btn_stopwords.grid(column=2, row=1)

        # Widget tham so model
        ttk.Label(self, text='Tham số:').grid(column=0, row=2, sticky='e')
        self.txt_params = tk.Text(self, width=50, height=10)
        self.txt_params.grid(column=1, row=2, padx=10, pady=5, sticky='wens')
        self.txt_params.delete(1.0, tk.END)
        self.txt_params.insert(tk.END, WORD_CLOUD_DEFAULT_PARAMS)

        # Widget nut ve word cloud
        self.btn_draw = ttk.Button(self, text='Vẽ word cloud', command=self.draw)
        self.btn_draw.grid(column=1, row=3, sticky='we', padx=10, pady=5)

        self.grid_columnconfigure(1, weight=1)

    def draw(self):
        if not self.validate_inputs():
            messagebox.showwarning('Thông báo', 'Bạn nhập thiếu thông tin!')
            return
        
        cluster_file = self.ent_doc.get()
        stopwords_file = self.ent_stopwords.get()
        params = json.loads(self.txt_params.get('1.0', 'end-1c'))
        
        draw_word_cloud(cluster_file, stopwords_file, params)

    def validate_inputs(self):
        required_fields = [
            self.ent_doc.get(),
            self.txt_params.get('1.0', 'end-1c'),
        ]
        return all(field for field in required_fields)