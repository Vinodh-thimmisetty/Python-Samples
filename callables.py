class SomeClass:

    def __init__(self):
        self._property = 'property'

    def __call__(self, *args, **kwargs):
        print('Allows all its instances as Callable()')

    def some_method(self, *args, **kwargs):
        self._property = 'update property'
        print('Method(s) associated to Class are callable')


def hyper_volume(length, *other_sides, **side_options):
    """
    Function(s) associated to Module are callable
        `*`  Destruct Positional-Args
        `**` Destruct Keyword-Args
        [length] ==> Mandatory arg
    """
    print(f'Sides : ', other_sides)
    print(f'Options: ', side_options)
    vol = length
    for side in other_sides:
        vol *= side
    print(f"Volume: [{vol}]")
    return vol


def extended_args(a, b, /, c=None, d=None, *, e, f):
    """
    Function(s) associated to Module are callable
        [a,b] ==> Position only arguments
        [e,f] ==> Key only arguments
        [c,d] ==> Optional arguments

        `/` [All Argument(s) "BEFORE" are Required and must be positional-only args]
        `*` [Any Argument(s) "AFTER"  are Required and must be Keyword-only args]
    """
    print(a, b, c, d, e, f)


if __name__ == '__main__':
    # conditional Expressions
    print('Old' if 60 > 20 else 'Young')
    print(f'Is Lambda callable:: {callable(lambda x: x ** 2)}  [unnamed callable]')
    print(f'Function(s) associated to Module are callable :  {callable(hyper_volume)}')
    print(f'Class is a callable() due to its parent "type" : {callable(SomeClass)}')
    sc = SomeClass()
    print(f'Is Instance(s) associated to Class are callable: {callable(sc)} [ # depends on __call__() in Class]')
    print(f'Method(s) associated to Class are callable: {callable(sc.some_method)}')

    hyper_volume(10, 20, 30, 40)
    # sides = (20, 30, 40)
    # length,breadth,height = (20, 30, 40)
    # length,_,height = (20, 30, 40)
    # length,*_,height = (20, 30, 40)
    # len,*_ = (20, 30, 40)
    # *_,breadth,height = (20, 30, 40)
    # hyper_volume(20, *sides)
    hyper_volume(20, *(20, 30, 40))
    # options = {'a': 'Area', 'v': 'Volume'}
    # hyper_volume(20, *sides, **options)
    hyper_volume(20, *(20, 30, 40), **{'a': 'Area', 'v': 'Volume'})
    #  Valid
    extended_args(1, 2, 3, 4, e=5, f=6)
    extended_args(1, 2, 3, e=5, f=6)
    extended_args(1, 2, e=5, f=6)
    # Invalid
    extended_args(a=1, b=2, e=5, f=6)
    extended_args(1, b=2, e=5, f=6)
    extended_args(1, 2, 5, f=6)
    extended_args(1, 2, 5, 6)
