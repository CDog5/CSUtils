class KVPair:
    def __init__(self,k,v):
        self.key = k
        self.value = v
    @property
    def as_dict(self):
        return {k:v}

class CustomDict:
    def __init__(self,**kwargs):
        myargs={}
        for k,v in kwargs.items():
            myargs[k] = KVPair(k,v)
        self.__dict__.update(myargs)
    def items(self):
        for k,v in self.__dict__.items():
            yield k,v.value
    def displaydict(self):
        tmpdict={}
        for k,v in self.items():
            tmpdict[k] = v
        return tmpdict
    def __str__(self):
        return f'{self.displaydict()}'
    def set(self,kvpair):
        self.__dict__[kvpair.key] = kvpair
    def remove(self,kvpair):
        del self.__dict__[kvpair.key]
##c = CustomDict(a=5,b=3)
##c.set(KVPair('a',4))
##print(c)
##for k,v in c.items():
##    print(k,v)
class Enum:
    def __init__(self,*args,**kwargs):
        if kwargs:
            x = max(kwargs.values()) + 1
        else:
            x = 0
        tmpdict = {}
        for arg in args:
            tmpdict[arg] = x
            x += 1
        z = tmpdict.copy()
        z.update(kwargs)
        self.__dict__.update(z)
        self.__state = 0
    def set(self,state):
        if state in self.__dict__.values():
            self.__state = state
    def get(self):
        return self.__state
    def next(self):
        if self.__state + 1 in self.__dict__.values():
            self.__state += 1
        else:
            self.__state = 0
    def __str__(self):
        return f'{self.__dict__}'

##e = Enum('CAT','DOG',a=0)
##print(e)
##print(e.CAT)
