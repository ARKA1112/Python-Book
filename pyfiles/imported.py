def f1(a, b): print(a, b)
def f2(a, *b): print(a, b)# Normal args
# Positional varargs
def f3(a, **b): print(a, b)# Keyword varargs
def f4(a, *b, **c): print(a, b, c)# Mixed modes
def f5(a, b=2, c=3): print(a, b, c)# Defaults
def f6(a, b=2, *c): print(a, b, c)# Defaults and positional varargs