import json, pickle
class UrlPage:
    def __init__(self,url):
        self.url = url
        if '?' in self.url:
            tmp = self.url.replace('&','?')
            tmp = tmp.split('?')
            self.mainpage = tmp[0]
            self.queries = tmp[1:]
        else:
            self.mainpage = self.url
            self.queries=[]
class UrlDomain:
    def __init__(self,url):
        self.url = url
        tmp = self.url.split('.')
        self.tld = tmp[-1]
        self.domain = tmp[-2]
        self.subs = tmp[:-2]
class UrlMethod:
    def __init__(self,method):
        self.type = method
class UrlParser:
    def __init__(self,url):
        self.url = url
        self.urllist = []
    def make_pages(self,pages):
        tmp = []
        for page in pages:
            tmp.append(UrlPage(page))
        return tmp
    def parse(self):
        self.method, tmp = self.url.split('://')
        self.method = UrlMethod(self.method)
        tmp = tmp.split('/')
        self.domain = UrlDomain(tmp[0])
        self.pages = self.make_pages(tmp[1:])
        self.urllist.extend([self.method,self.domain.url,*[x.url for x in self.pages]])
        return (self.method,self.domain,self.pages)
class FileParser:
    def __init__(self,filepath):
        self.fp = filepath
        self.contents = self.load_contents()
        if self.fp.endswith('.json'):
            self.parsed =  json.loads(self.contents)
        elif self.fp.endswith('.p'):
            self.parsed = pickle.load( open( self.fp, "rb" ) )
        else:
            self.parsed = self.contents
    def load_contents(self):
        with open(self.fp,'r') as f:
            return f.read()          
