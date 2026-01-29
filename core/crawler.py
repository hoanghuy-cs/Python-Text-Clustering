import requests
from bs4 import BeautifulSoup

class CorpusCrawler():
    def __init__(self):
        pass

    def crawlFromTuoiTre(self, resource, output_file):
        try:
            response = requests.get('https://tuoitre.vn/' + resource + '.htm')
            soup = BeautifulSoup(response.content, "html.parser")
            titles = soup.findAll('h3', class_='box-title-text')
            links = [link.find('a').attrs["href"] for link in titles]
            file = open(output_file, 'w', encoding='utf-8')
            for link in links:
                news = requests.get("https://tuoitre.vn" + link)
                soup = BeautifulSoup(news.content, "html.parser")
                # title = soup.find("h1", class_="article-title").text
                body = soup.find("div", class_="detail-content")
                content = body.findChildren("p", recursive=False)[0].text + body.findChildren("p", recursive=False)[1].text
                file.write(content + '\n')
            file.close()
            return True
        except:
            return False
        
    def crawlFromThanhNien(self, resource, output_file):
        #try:
            response = requests.get('https://thanhnien.vn/' + resource + '.htm')
            soup = BeautifulSoup(response.content, "html.parser")
            titles = soup.findAll('h3', class_='box-title-text')
            links = [link.find('a').attrs["href"] for link in titles]
            file = open(output_file, 'w', encoding='utf-8')
            for link in links:
                news = requests.get("https://thanhnien.vn" + link)
                soup = BeautifulSoup(news.content, "html.parser")
                body = soup.find("div", class_="detail-content")
                content = body.findChildren("p", recursive=False)[0].text + body.findChildren("p", recursive=False)[1].text
                file.write(content + '\n')
            file.close()
            return True
        #except:
        #    return False