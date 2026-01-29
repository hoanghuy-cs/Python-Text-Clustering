import tkinter as tk
from tkinter import messagebox, ttk
from core.convert import CorpusConverter
from gui.common import choose_dir, choose_file
import os

class TabConvert(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.master = master

        ttk.Label(self, text='(Chuyển đổi ngữ liệu PDF, DOCX sang file text)')\
            .grid(column=1, row=0, padx=10, sticky='w')

        # Widget chon file ngu lieu
        ttk.Label(self, text='File ngữ liệu:').grid(column=0, row=1, sticky='e')
        self.ent_source = ttk.Entry(self)
        self.ent_source.grid(column=1, row=1, sticky='we', padx=10, pady=5)
        self.btn_source = ttk.Button(self, text='Chọn', command=lambda: choose_file(self.ent_source))
        self.btn_source.grid(column=2, row=1)

        # Widget chon thu muc xuat
        ttk.Label(self, text='Thư mục lưu:').grid(column=0, row=2, sticky='e')
        self.ent_output_dir = ttk.Entry(self)
        self.ent_output_dir.grid(column=1, row=2, sticky='we', padx=10, pady=5)
        self.btn_output_dir = ttk.Button(self, text='Chọn', command=lambda: choose_dir(self.ent_output_dir))
        self.btn_output_dir.grid(column=2, row=2)

        # Widget ten file luu
        ttk.Label(self, text='Tên file lưu:').grid(column=0, row=3, sticky='e')
        self.ent_file_name = ttk.Entry(self)
        self.ent_file_name.grid(column=1, row=3, sticky='we', padx=10, pady=5)

        # Widget nut chuyen doi
        self.btn_convert = ttk.Button(self, text='Chuyển đổi', command=self.convert)
        self.btn_convert.grid(column=1, row=4, sticky='we', padx=10, pady=5)

        self.img_convert = tk.PhotoImage(file='img/convert.png')
        ttk.Label(self, image=self.img_convert).grid(column=1, row=5, pady=10)

        self.grid_columnconfigure(1, weight=1)

    def validate_inputs(self):
        required_fields = [
            self.ent_source.get(),
            self.ent_output_dir.get(),
            self.ent_file_name.get(),
        ]
        return all(field for field in required_fields)

    def convert(self):
        if not self.validate_inputs():
            messagebox.showwarning('Thông báo', 'Bạn nhập thiếu thông tin!')
            return
        
        is_success = False
        try:
            source_ext = os.path.splitext(self.ent_source.get())[1].upper()
            output_file = os.path.join(self.ent_output_dir.get(), self.ent_file_name.get())
            converter = CorpusConverter()
            if source_ext == '.PDF':
                is_success = converter.from_pdf(self.ent_source.get(), output_file)
            if source_ext == '.DOCX':
                is_success = converter.from_docx(self.ent_source.get(), output_file)
        except:
            pass

        if is_success: messagebox.showinfo('Thông báo', 'Chuyển đổi thành công!')
        else: messagebox.showerror('Thông báo', 'Có lỗi xảy ra, hãy kiểm tra lại thông tin.')