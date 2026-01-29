from tkinter import messagebox, ttk
import tkinter as tk
import os
from core.cleaner import CorpusCleaner
from gui.common import choose_dir, choose_file

class TabClean(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.master = master

        self.rem_link = tk.BooleanVar()
        self.to_lower = tk.BooleanVar()
        self.rem_sym = tk.BooleanVar()
        self.rem_punc = tk.BooleanVar()
        self.rem_num = tk.BooleanVar()
        self.rem_space = tk.BooleanVar()
        self.rem_sw = tk.BooleanVar()

        # Widget chon file ngu lieu
        ttk.Label(self, text='File ngữ liệu:').grid(column=0, row=0, sticky='e')
        self.ent_source = ttk.Entry(self)
        self.ent_source.grid(column=1, row=0, sticky='we', padx=10, pady=5)
        self.btn_source = ttk.Button(self, text='Chọn', command=lambda: choose_file(self.ent_source))
        self.btn_source.grid(column=2, row=0)

        # Widget chon file ngu lieu
        ttk.Label(self, text='File stopwords:').grid(column=0, row=1, sticky='e')
        self.ent_stopword = ttk.Entry(self)
        self.ent_stopword.grid(column=1, row=1, sticky='we', padx=10, pady=5)
        self.btn_stopword = ttk.Button(self, text='Chọn', command=lambda: choose_file(self.ent_stopword))
        self.btn_stopword.grid(column=2, row=1)

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

        # Cac checkbox
        self.chk_to_lower = ttk.Checkbutton(self, text='Chuyển sang chữ thường', variable=self.to_lower)
        self.chk_to_lower.grid(column=1, row=4, sticky='w', padx=10)

        self.chk_rem_link = ttk.Checkbutton(self, text='Xóa đường link', variable=self.rem_link)
        self.chk_rem_link.grid(column=1, row=5, sticky='w', padx=10)

        self.chk_rem_sym = ttk.Checkbutton(self, text='Xóa ký tự đặc biệt', variable=self.rem_sym)
        self.chk_rem_sym.grid(column=1, row=6, sticky='w', padx=10)

        self.chk_rem_punc = ttk.Checkbutton(self, text='Xóa dấu câu', variable=self.rem_punc)
        self.chk_rem_punc.grid(column=1, row=7, sticky='w', padx=10)

        self.chk_rem_num = ttk.Checkbutton(self, text='Xóa số', variable=self.rem_num)
        self.chk_rem_num.grid(column=1, row=8, sticky='w', padx=10)

        self.chk_rem_space = ttk.Checkbutton(self, text='Xóa khoảng trắng thừa', variable=self.rem_space)
        self.chk_rem_space.grid(column=1, row=9, sticky='w', padx=10)

        self.chk_rem_sw = ttk.Checkbutton(self, text='Xóa stopwords', variable=self.rem_sw)
        self.chk_rem_sw.grid(column=1, row=10, sticky='w', padx=10)

        # Widget nut chuyen doi
        self.btn_convert = ttk.Button(self, text='Làm sạch', command=self.clean)
        self.btn_convert.grid(column=1, row=11, sticky='we', padx=10, pady=5)

        self.grid_columnconfigure(1, weight=1)

    def validate_inputs(self):
        required_fields = [
            self.ent_source.get(),
            self.ent_output_dir.get(),
            self.ent_file_name.get()
        ]
        return all(field for field in required_fields)

    def clean(self):
        if not self.validate_inputs():
            messagebox.showwarning('Thông báo', 'Bạn nhập thiếu thông tin!')
            return
        
        cleaner = CorpusCleaner()
        is_success = cleaner.clean(
            src_file=self.ent_source.get(),
            output_file=os.path.join(self.ent_output_dir.get(), self.ent_file_name.get()),
            to_lower=self.to_lower.get(),
            rem_link=self.rem_link.get(),
            rem_sym=self.rem_sym.get(),
            rem_punc=self.rem_punc.get(),
            rem_num=self.rem_num.get(),
            rem_space=self.rem_space.get(),
            rem_sw=self.rem_sw.get(),
            sw_file=self.ent_stopword.get()
        )

        if is_success: messagebox.showinfo('Thông báo', 'Làm sạch thành công!')
        else: messagebox.showerror('Thông báo', 'Có lỗi xảy ra, hãy kiểm tra lại thông tin.')