
import typing
import ascii_grapher_validations


class GraphStruct:
    @classmethod
    @ascii_grapher_validations.sigmoid_validate
    def plot_sigmoid(cls, domain, co_domain, **kwargs):

        graph = [[' ' if b else '|' for b in range(*domain)] if c else ['_' for _ in range(*domain)] for c in range(*co_domain)][::-1]
        for i in range(*domain):
            _result = int(ascii_grapher_validations.sigmoid(i, *[kwargs[c] for c in ascii_grapher_validations.sigmoid.__annotations__['return']]))
            try:
                graph[_result][i] = '*'
            except:
                pass
        return '\n'.join(''.join(i) for i in graph)

    @classmethod
    @ascii_grapher_validations.linear_validate
    def plot_linear(cls, domain, co_domain, **kwargs):

        graph = [[' ' if b else '|' for b in range(*domain)] if c else ['_' for _ in range(*domain)] for c in range(*co_domain)][::-1]
        for i in range(*domain):
            _result = int(ascii_grapher_validations.linear(i, *[kwargs[c] for c in ascii_grapher_validations.linear.__annotations__['return']]))
            try:
                graph[_result][i] = '*'
            except:
                pass
        return '\n'.join(''.join(i) for i in graph)

class Grapher:
    @ascii_grapher_validations.validate_graph_type
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs

    @ascii_grapher_validations.has_a_b
    def plot(self, **kwargs):
        self.kwargs.update(kwargs)
        print(getattr(GraphStruct, 'plot_{}'.format(self.kwargs.get('type')))(self.kwargs.get('domain'), self.kwargs.get('co_domain'), **self.kwargs))

    def _load_params(self, **kwargs):
        self.kwargs.update(kwargs)

    def __call__(self, _x):

        return ascii_grapher_validations.full_functions[self.kwargs.get('type').lower()](_x, *[self.kwargs[i] for i in ascii_grapher_validations.full_functions[self.kwargs.get('type').lower()].__annotations__['return']])

    def __repr__(self):
        return "<graph of type '{type}' defined on D:{domain}, R:{co_domain}>".format(**self.kwargs)

if __name__ == '__main__':
    #g = Grapher(type='sigmoid', domain=[-30, 30], co_domain=[-30, 30])
    #g.plot(a = 0.3, b = 1, shift = 0, c = 25)
    g = Grapher(type='linear', domain=[-30, 30], co_domain = [-30, 30])
    g.plot(m=1, b=0)
