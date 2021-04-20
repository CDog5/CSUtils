import math
class CompressedList:
    def __init__(self,items):
        tmp=[]
    
        for i,item in enumerate(self.unpack(items)):
            a = len(tmp) - 1
            if a == -1:
                tmp.append([item,1])
            elif tmp[a][0] == item:
               tmp[a][1] += 1
            else:
                tmp.append([item,1])
        self.items = tmp
    def negative_normalise(self):
        out = []
        for item in self.items:
            out.append(-math.sqrt(item[0]**2))
        return out
    def normalise(self):
        out = []
        for item in self.items:
            out.append(math.sqrt(item[0]**2))
        return out
    def unpack(self,items):
        out = []
        for item in items:
            if isinstance(item,list):
                out.extend(self.unpack(item))
            elif isinstance(item,tuple):
                out.extend(self.unpack(item))
            elif isinstance(item,set):
                out.extend(self.unpack(item))
            else:
                out.append(item)
        return out
    def __repr__(self):
        return f'{self.items}'
    def median(self):
        items = sorted(self.items)
        l = float(len(items)-1)
        l = l/2
        if l.is_integer():
            return items[int(l)][0]
        else:
            low = items[math.floor(l)][0]
            high = items[math.ceil(l)][0]
            l = (high + low) / 2
            return l
    def mode(self):
        self.items = sorted(self.items,key=lambda x: x[1],reverse=True)
        last = self.items[0][1]
        out=[]
        for item in self.items:
            if item[1] == last:
                out.append(tuple(item))
        return out
    #sum compressed list without decompression
    def sum_compress(self):
        total = 0
        for item in self.items:
            total += item[0]*item[1]
        return total
    def len_compress(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total
    def mean(self):
        return self.sum_compress(self) / self.len_compress(self)
    #decompresses stuff compressed by the function above
    def decompress(self):
        tmp =[]
        for item in self.items:
            for _ in range(item[1]):
                tmp.append(item[0])
        return tmp
    def remove_duplicates(self):
        return list(set(self.items))
def mean(inlist):
    return sum(inlist) / len(inlist)
def median(inlist):
    return CompressedList(inlist).median()
def mode(inlist):
    return CompressedList(inlist).mode()[0][0]
def remove_duplicates(self,inlist):
    return list(set(inlist))

#this version does have to load the list again and use it
def eping_pong(inlist,stop=None):
    lst = inlist+list(reversed(inlist[1:-1]))
    iters=0
    i = 0
    while True:
        if stop:
            if iters >= stop:
                break
        if i >= len(lst):
            i = 0
        yield lst[i]
        i += 1
        iters +=1

#this is usually slower but doesn't have to write a new list
def ping_pong(inlist,stop=None):
    iters = 0
    incr = 1
    i = 0
    while True:
        if stop:
            if iters >= stop:
                break
        if i >= len(inlist):
            i -=2
            incr = -1
        elif i < 1:
            i = 0
            incr = 1
        yield inlist[i]
        i += incr
        
        iters +=1
#goes through list, then goes back to list[0]
def loop(inlist,stop=None):
    iters=0
    i = 0
    while True:
        if stop:
            if iters >= stop:
                break
        if i >= len(inlist):
            i = 0
        yield inlist[i]
        i += 1
        iters +=1
