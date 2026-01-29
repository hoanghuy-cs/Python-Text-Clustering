import re
import string
import os
from nltk.tokenize import word_tokenize
from core.common import read_file
from nltk.corpus import stopwords

class CorpusCleaner():
    def __init__(self):
        pass

    def clean(self, src_file, output_file, to_lower, rem_link, rem_sym, rem_punc, rem_num, rem_space, rem_sw, sw_file=None):
        try:
            org_corpus = read_file(src_file)
            
            stopwords = []
            if (rem_sw == True) and (sw_file != None) and os.path.exists(sw_file):
                stopwords = read_file(sw_file)

            f = open(output_file, 'w', encoding='utf-8')
            for i in range(len(org_corpus)):
                if to_lower == True:
                    org_corpus[i] = org_corpus[i].lower()
                if rem_sw == True and len(stopwords) > 0:
                    org_corpus[i] = self.rem_stopword(org_corpus[i], stopwords)
                if rem_link == True:
                    org_corpus[i] = re.sub(r'(?:http|ftp|https)://(?:[\w_-]+(?:(?:\.[\w_-]+)+))(?:[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '', org_corpus[i])
                if rem_sym == True:
                    org_corpus[i] = re.sub(r'(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])', '', org_corpus[i])
                if rem_punc == True:
                    org_corpus[i] = re.sub(f'[{re.escape(string.punctuation)}]', '', org_corpus[i])
                if rem_num == True:
                    org_corpus[i] = re.sub(r'(\d+)', ' ', org_corpus[i])
                if rem_space == True:
                    org_corpus[i] = re.sub(r'(\s+)', ' ', org_corpus[i])
                    org_corpus[i] = org_corpus[i].strip()
                f.write(org_corpus[i] + '\n')
            f.close()
            return True
        except:
            return False

    def rem_stopword(self, text: str, stopwords: list) -> str:
        words = word_tokenize(text)
        filtered = [w for w in words if not w.lower() in stopwords]
        return ' '.join(filtered)