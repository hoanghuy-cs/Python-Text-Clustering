import tkinter as tk
from tkinter import messagebox, ttk
from core.common import SOURCES_CRAWL
from core.crawler import CorpusCrawler
from gui.common import choose_dir
import os

class TabCrawl(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.master = master

        # Widget chọn nguồn dữ liệu
        ttk.Label(self, text='Nguồn ngữ liệu:').grid(column=0, row=0, sticky='e')
        self.cbx_source = ttk.Combobox(self, state='readonly', values=SOURCES_CRAWL)
        self.cbx_source.grid(column=1, row=0, sticky='we', padx=10, pady=5)

        # Widget chon thu muc xuat
        ttk.Label(self, text='Thư mục lưu:').grid(column=0, row=1, sticky='e')
        self.ent_output_dir = ttk.Entry(self)
        self.ent_output_dir.grid(column=1, row=1, sticky='we', padx=10, pady=5)
        self.btn_output_dir = ttk.Button(self, text='Chọn', command=lambda: choose_dir(self.ent_output_dir))
        self.btn_output_dir.grid(column=2, row=1)

        # Widget ten file luu
        ttk.Label(self, text='Tên file lưu:').grid(column=0, row=2, sticky='e')
        self.ent_file_name = ttk.Entry(self)
        self.ent_file_name.grid(column=1, row=2, sticky='we', padx=10, pady=5)

        # Widget nut cao
        self.btn_crawl = ttk.Button(self, text='Bắt đầu cào', command=self.crawl)
        self.btn_crawl.grid(column=1, row=3, sticky='we', padx=10, pady=5)

        self.img_tuoitre = tk.PhotoImage(file='img/tuoitre.png')
        ttk.Label(self, image=self.img_tuoitre).grid(column=1, row=4, pady=10)

        self.img_thanhnien = tk.PhotoImage(file='img/thanhnien.png')
        ttk.Label(self, image=self.img_thanhnien).grid(column=1, row=5, pady=10)

        self.grid_columnconfigure(1, weight=1)

    def validate_inputs(self):
        required_fields = [
            self.cbx_source.get(),
            self.ent_output_dir.get(),
            self.ent_file_name.get(),
        ]
        return all(field for field in required_fields)

    def crawl(self):
        if not self.validate_inputs():
            messagebox.showwarning('Thông báo', 'Bạn nhập thiếu thông tin!')
            return
        
        crawler = CorpusCrawler()
        output_file = os.path.join(self.ent_output_dir.get(), self.ent_file_name.get())

        is_success = False
        
        if self.cbx_source.get() == 'Báo Tuổi trẻ (Tin mới nhất)':
            is_success = crawler.crawlFromTuoiTre('tin-moi-nhat', output_file)
        elif self.cbx_source.get() == 'Báo Tuổi trẻ (Thời sự)':
            is_success = crawler.crawlFromTuoiTre('thoi-su', output_file)
        elif self.cbx_source.get() == 'Báo Tuổi trẻ (Pháp luật)':
            is_success = crawler.crawlFromTuoiTre('phap-luat', output_file)
        elif self.cbx_source.get() == 'Báo Tuổi trẻ (Kinh doanh)':
            is_success = crawler.crawlFromTuoiTre('kinh-doanh', output_file)
        elif self.cbx_source.get() == 'Báo Tuổi trẻ (Xe)':
            is_success = crawler.crawlFromTuoiTre('xe', output_file)
        elif self.cbx_source.get() == 'Báo Tuổi trẻ (Du lịch)':
            is_success = crawler.crawlFromTuoiTre('du-lich', output_file)
        elif self.cbx_source.get() == 'Báo Tuổi trẻ (Nhịp sống trẻ)':
            is_success = crawler.crawlFromTuoiTre('nhip-song-tre', output_file)
        elif self.cbx_source.get() == 'Báo Tuổi trẻ (Văn hóa)':
            is_success = crawler.crawlFromTuoiTre('van-hoa', output_file)
        elif self.cbx_source.get() == 'Báo Tuổi trẻ (Giải trí)':
            is_success = crawler.crawlFromTuoiTre('giai-tri', output_file)
        elif self.cbx_source.get() == 'Báo Tuổi trẻ (Giáo dục)':
            is_success = crawler.crawlFromTuoiTre('giao-duc', output_file)
        elif self.cbx_source.get() == 'Báo Tuổi trẻ (Nhà đất)':
            is_success = crawler.crawlFromTuoiTre('nha-dat', output_file)
        elif self.cbx_source.get() == 'Báo Tuổi trẻ (Sức khỏe)':
            is_success = crawler.crawlFromTuoiTre('suc-khoe', output_file)
        elif self.cbx_source.get() == 'Báo Tuổi trẻ (Giả thật)':
            is_success = crawler.crawlFromTuoiTre('gia-that', output_file)
        elif self.cbx_source.get() == 'Báo Tuổi trẻ (Bạn đọc làm báo)':
            is_success = crawler.crawlFromTuoiTre('ban-doc-lam-bao', output_file)

        elif self.cbx_source.get() == 'Báo Thanh niên (Tin mới nhất)':
            is_success = crawler.crawlFromThanhNien('tin-moi-nhat', output_file)
        elif self.cbx_source.get() == 'Báo Thanh niên (Thời sự)':
            is_success = crawler.crawlFromThanhNien('thoi-su', output_file)
        elif self.cbx_source.get() == 'Báo Thanh niên (Sức khỏe)':
            is_success = crawler.crawlFromThanhNien('suc-khoe', output_file)
        elif self.cbx_source.get() == 'Báo Thanh niên (Giới trẻ)':
            is_success = crawler.crawlFromThanhNien('gioi-tre', output_file)
        elif self.cbx_source.get() == 'Báo Thanh niên (Văn hóa)':
            is_success = crawler.crawlFromThanhNien('van-hoa', output_file)
        elif self.cbx_source.get() == 'Báo Thanh niên (Xe)':
            is_success = crawler.crawlFromThanhNien('xe', output_file)
        else:
            is_success = False

        if is_success: messagebox.showinfo('Thông báo', 'Cào dữ liệu thành công!')
        else: messagebox.showerror('Thông báo', 'Có lỗi xảy ra, hãy kiểm tra lại thông tin.')