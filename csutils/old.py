import requests,json
if __name__ != '__main__':
    print('This is old and will be removed soon!')
class Modes:
    def __init__(self):
        self.APIMODE_NOKEY = 0
        self.APIMODE_KEY = 1
        self.APIMODE_OAUTH = 2 
modes = Modes()
class Api:
    def init(self,url,mode):
        self.url = url
        self.mode = mode
    def get_data(self,args):
        if self.mode == modes.APIMODE_NOKEY:
            if args == []:
                a = self.url
            else:
                a = f"{self.url}?{args[0]}"
                for i in range(1,len(args)):
                    a += f"&{args[i]}"
                
            r = requests.get(a)
            return json.loads(r.text)
        return None
class Computing:
    def ping(self):
       print("Pong!")
    def remove_duplicates(self,list1):
        a = set(list1)
        a = list(a)
        return a
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
class Math:
    def fibonacci(self,start_no,length):
        sequence=[]
        n1, n2 = start_no, start_no
        for _ in range(0,length):
           sequence.append(n1)
           nth = n1 + n2
           n1 = n2
           n2 = nth
        return sequence
    def is_prime(self,num):
        for i in range(2,num):
           if (num % i) == 0:
               return False
        return True
    def factorial(self,num):
        count = num-1
        while count > 1:
            num = num * count
            count -=1
        return num
    def km_to_mi(self,no):
        return no * 0.621371
    def mi_to_km(self,no):
        return no / 0.621371
    def c_to_f(self,no):
        fahrenheit = (no * 1.8) + 32
        return fahrenheit
    def f_to_c(self,no):
        celsius = (no / 1.8) - 32
        return celsius
computing = Computing()
math = Math()
api = Api()
