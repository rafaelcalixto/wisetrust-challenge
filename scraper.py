####### Python 3.6
####### author: Rafael Calixto
####### created at: 08/26/2018
####### description: This library provide a web crawler to extract
####### informations from web pages.
from urllib import request as r

class Scraper():
    def __init__(self):
        self.headers = {}
        self.headers['User-Agent'] = '''Mozilla/5.0 (X11; Linux 1686)
        AppleWebKit/537.17 (KHTML, like Gecko)
        Chrome/24.0.1312.27 Safari/537.17'''.replace('\n','')
        self.err = None
        self.data = None

    def get_it(self, url):
        ### input: str
        ### output: str, str {error}
        try:
            self.data = r.urlopen(r.Request(url, headers = self.headers)).read()
        except Exception as e:
            self.err = 'Erro ao acessar a URL:' + url + '\n' + e

        return str(self.data), self.err
