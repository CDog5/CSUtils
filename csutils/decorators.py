import time
class timed:
    def __init__(self,amnt=1):
        self.repeats = amnt
    def __call__(self,f):
        def inner(*args,**kwargs):
            times=[]
            f1 = time.perf_counter()
            print(f'Timing function {f.__name__}')
            for i in range(self.repeats):
                t1 = time.perf_counter()
                if not args and not kwargs:
                    func = f()
                elif not args:
                    func = f(kwargs)
                else:
                    func = f(args)
                t2 = time.perf_counter()
                times.append(t2-t1)
            avg = sum(times)/len(times)
            f2 = time.perf_counter()
            print(f'Took {f2-f1} secs. Average {avg} secs.')
        return inner
