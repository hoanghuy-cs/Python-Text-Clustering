import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from core.dbscan import DBSCANModel
from core.dbscandoc2vec import DBSCANDoc2Vec
from core.kmeans import KMeansModel
from core.kmeansdoc2vec import KMeansDoc2Vec
from core.kmeansword2vec import KMeansWord2Vec
from gui.common import choose_file, choose_dir
from core.common import MODELS, MODELS_PREDICTING_CONFIGS

class TabPredict(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.master = master

        # Widget chon file ngu lieu
        ttk.Label(self, text='File ngữ liệu:').grid(column=0, row=0, sticky='e')
        self.ent_corpus = ttk.Entry(self)
        self.ent_corpus.grid(column=1, row=0, sticky='we', padx=10, pady=5)
        self.btn_corpus = ttk.Button(self, text='Chọn', command=lambda: choose_file(self.ent_corpus))
        self.btn_corpus.grid(column=2, row=0)

        # Widget chon file stopword
        ttk.Label(self, text='File stopword:').grid(column=0, row=1, sticky='e')
        self.ent_stopword = ttk.Entry(self)
        self.ent_stopword.grid(column=1, row=1, sticky='we', padx=10, pady=5)
        self.btn_stopword = ttk.Button(self, text='Chọn', command=lambda: choose_file(self.ent_stopword))
        self.btn_stopword.grid(column=2, row=1)

        # Widget chon duong dan luu
        ttk.Label(self, text='Thư mục lưu:').grid(column=0, row=2, sticky='e')
        self.ent_output_dir = ttk.Entry(self)
        self.ent_output_dir.grid(column=1, row=2, sticky='we', padx=10, pady=5)
        self.btn_output_dir = ttk.Button(self, text='Chọn', command=lambda: choose_dir(self.ent_output_dir))
        self.btn_output_dir.grid(column=2, row=2)

        # Widget chon model
        ttk.Label(self, text='Chọn mô hình:').grid(column=0, row=3, sticky='e')
        self.cbx_model = ttk.Combobox(self, state='readonly', values=MODELS)
        self.cbx_model.bind('<<ComboboxSelected>>', self.on_change_model)
        self.cbx_model.grid(column=1, row=3, sticky='we', padx=10, pady=5)

        # Widget tham so model
        ttk.Label(self, text='Tham số:').grid(column=0, row=4, sticky='e')
        self.txt_params = tk.Text(self, width=50, height=10)
        self.txt_params.grid(column=1, row=4, padx=10, pady=5, sticky='wens')

        # Widget nut predict
        self.btn_predict = ttk.Button(self, text='Dự đoán', command=self.predict)
        self.btn_predict.grid(column=1, row=5, sticky='we', padx=10, pady=5)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(4, weight=1)

    def on_change_model(self, event):
        self.txt_params.delete(1.0, tk.END)
        self.txt_params.insert(tk.END, MODELS_PREDICTING_CONFIGS[self.cbx_model.get()])

    def validate_inputs(self):
        required_fields = [
            self.ent_corpus.get(),
            self.ent_stopword.get(),
            self.ent_output_dir.get(),
            self.txt_params.get('1.0', 'end-1c'),
        ]
        return all(field for field in required_fields)

    def predict(self):
        if not self.validate_inputs():
            messagebox.showwarning('Thông báo', 'Bạn nhập thiếu thông tin!')
            return
        
        model_name = self.cbx_model.get()
        corpus_file = self.ent_corpus.get()
        stopwords_file = self.ent_stopword.get()
        output_dir = self.ent_output_dir.get()
        params = json.loads(self.txt_params.get('1.0', 'end-1c'))
        
        is_success = False
        
        if model_name == 'KMeans (TF-IDF)':
            kmeans_model = KMeansModel()
            vectorizer_file = params['vectorizer']
            model_file = params['model_file']
            is_success = kmeans_model.predict(corpus_file, stopwords_file, vectorizer_file, model_file, output_dir)
        elif model_name == 'KMeans (Doc2Vec)':
            kmeans_model = KMeansDoc2Vec()
            d2v_file = params['d2v_file']
            model_file = params['kmeans_file']
            is_success = kmeans_model.predict(corpus_file, stopwords_file, d2v_file, model_file, output_dir)
        elif model_name == 'KMeans (Word2Vec)':
            kmeans_model = KMeansWord2Vec()
            w2v_file = params['w2v_file']
            model_file = params['kmeans_file']
            is_success = kmeans_model.predict(corpus_file, stopwords_file, w2v_file, model_file, output_dir)
        elif model_name == 'DBSCAN (TF-IDF)':
            dbscan_model = DBSCANModel()
            is_success = dbscan_model.predict(corpus_file, stopwords_file, params, output_dir)
        elif model_name == 'DBSCAN (Doc2Vec)':
            dbscan_model = DBSCANDoc2Vec()
            is_success = dbscan_model.predict(corpus_file, stopwords_file, params, output_dir)
        
        if is_success: messagebox.showinfo('Thông báo', 'Dự đoán đã hoàn tất!')
        else: messagebox.showerror('Thông báo', 'Có lỗi xảy ra, hãy kiểm tra lại thông tin.')