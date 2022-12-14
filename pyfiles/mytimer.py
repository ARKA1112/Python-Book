import time, sys
trace = lambda *args: None
timefunc = time.time if sys.platform[:3]=='lin' else time.clock_getres

def timer(func, *args, _reps=1000,**kwargs):
    trace()
    start = timefunc()
    for i in range(_reps):
        ret = func(*args,**kwargs)
    elapsed = timefunc() - start
    return (elapsed, ret)

def best(func,*args,_reps = 50, **kwargs):
    best = 2**32
    for i in range(_reps):
        (time,ret) = timer(func,*args,_reps=1,**kwargs)
        if time<best:
            best = time
        return (time,ret)