from pypdf import PdfReader
import docx2txt

class CorpusConverter():
    def __init__(self):
        pass

    def from_pdf(self, source_file, output_file):
        try:
            reader = PdfReader(source_file)
            file = open(output_file, 'w', encoding='utf-8')
            for page in reader.pages:
                file.write(page.extract_text() + '\n')
            file.close
            return True
        except:
            return False

    def from_docx(self, source_file, output_file):
        try:
            src_file = open(source_file, 'rb')
            out_file = open(output_file, 'w', encoding='utf-8')
            out_file.write(docx2txt.process(src_file))
            out_file.close()
            src_file.close()
            return True
        except:
            return False