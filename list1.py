def append1(x):
    return x + [1]

def extend1(l):
    return l + [2, 3]

def pop0():
    l = [1, 2, 3]
    l.pop()
    return l

def remove1(x):
    l = [1, 2, 3, x]
    l.remove(x)
    return l
