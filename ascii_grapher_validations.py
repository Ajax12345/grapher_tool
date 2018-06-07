import math, re

def sigmoid(x, a:[int, float], b:[float, int], c:[int, float], shift:[int, float, None]=0) -> ['a', 'b', 'c', 'shift']:
    return c/float(1+(a*pow(math.e, -1*b*(x-shift))))

def linear(x, m:[int, float], b:[int, float]) -> ['m', 'b']:
    return (m*x) + b

def has_a_b(f):
    def wrapper(cls, *args, **kwargs):
        for i in ['domain', 'co_domain']:
            if i not in cls.kwargs:
                raise ValueError("missing '{}' needed to graph equation".format(i))
        return f(cls, *args, **kwargs)
    return wrapper

def validate_graph_type(f):
    def wrapper(cls, *args, **kwargs):
        if kwargs.get('type', '').lower() not in ['sigmoid', 'linear']:
            raise KeyError("missing graph type")
        return f(cls, *args, **kwargs)
    return wrapper

full_functions = {'sigmoid':sigmoid, 'linear':linear}
def sigmoid_validate(f):
    def wrapper(_, x, y, **kwargs):
        for i in full_functions[re.findall('[a-zA-Z]+$', f.__name__)[0]].__annotations__['return']:
            if i not in kwargs:
                raise TypeError("Graph type '{}' missing parameter '{}'".format(re.findall('[a-zA-Z]+$', f.__name__), i))
        return f(_, x, y, **{a:b for a, b in kwargs.items() if a not in ['domain', 'co_domain']})

    return wrapper

def linear_validate(f):
    def wrapper(_, x, y, **kwargs):
        for i in full_functions[re.findall('[a-zA-Z]+$', f.__name__)[0]].__annotations__['return']:
            if i not in kwargs:
                raise TypeError("Graph type '{}' missing parameter '{}'".format(re.findall('[a-zA-Z]+$', f.__name__), i))
        return f(_, x, y, **{a:b for a, b in kwargs.items() if a not in ['domain', 'co_domain']})

    return wrapper
