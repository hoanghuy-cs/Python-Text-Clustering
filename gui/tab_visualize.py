import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from core.visualize import visualize
from gui.common import choose_file
from core.common import PLOT_TYPES

class TabVisualize(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.master = master

        # Widget chon kieu bieu do
        ttk.Label(self, text='Chọn biểu đồ:').grid(column=0, row=0, sticky='e')
        self.cbx_plot = ttk.Combobox(self, state='readonly', values=PLOT_TYPES)
        self.cbx_plot.bind('<<ComboboxSelected>>', self.on_change_plot_type)
        self.cbx_plot.grid(column=1, row=0, sticky='we', padx=10, pady=5)

        # Widget chon file label
        ttk.Label(self, text='File label:').grid(column=0, row=1, sticky='e')
        self.ent_label = ttk.Entry(self)
        self.ent_label.grid(column=1, row=1, sticky='we', padx=10, pady=5)
        self.btn_label = ttk.Button(self, text='Chọn', command=lambda: choose_file(self.ent_label))
        self.btn_label.grid(column=2, row=1)

        # Widget chon file dac trung
        ttk.Label(self, text='File đặc trưng:').grid(column=0, row=2, sticky='e')
        self.ent_X_test = ttk.Entry(self)
        self.ent_X_test.grid(column=1, row=2, sticky='we', padx=10, pady=5)
        self.btn_X_test = ttk.Button(self, text='Chọn', command=lambda: choose_file(self.ent_X_test))
        self.btn_X_test.grid(column=2, row=2)

        # Widget nut predict
        self.btn_predict = ttk.Button(self, text='Trực quan hóa', command=self.visualize)
        self.btn_predict.grid(column=1, row=4, sticky='we', padx=10, pady=5)

        self.grid_columnconfigure(1, weight=1)

    def validate_inputs(self):
        required_fields = [
            self.ent_label.get(),
            self.cbx_plot.get()
        ]
        return all(field for field in required_fields)
    
    def visualize(self):
        if not self.validate_inputs():
            messagebox.showwarning('Thông báo', 'Bạn nhập thiếu thông tin!')
            return
        
        plot_type = self.cbx_plot.get()

        labels_file = self.ent_label.get()
        X_test_file = None if plot_type == 'Histogram' else self.ent_X_test.get()

        if not visualize(labels_file, X_test_file, plot_type):
            messagebox.showerror('Thông báo', 'Có lỗi xảy ra, hãy kiểm tra lại thông tin.')

    def on_change_plot_type(self, event):
        X_test_state = 'disable' if self.cbx_plot.get() == 'Histogram' else 'normal'
        self.ent_X_test['state'] = X_test_state
        self.btn_X_test['state'] = X_test_state