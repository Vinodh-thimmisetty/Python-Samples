g = 'global'
message = 100


def scoping_rules(e='enclosing'):
    """
        Scope Rules  = 'L'ocal'E'nclose'G'lobal'B'uiltin
    """
    l = 'local'
    message = 200
    print('Enclosing Message : ', message)

    def local_func():
        el = 'ELocal'
        # global message
        nonlocal message
        message = 300
        print(g, e, l, el)
        print('Local Message : ', message)

    local_func()
    print('Enclosing Message : ', message)


def sort_list(input):
    def sortby(item):
        return item[-1]

    return sorted(input, key=sortby)


if __name__ == '__main__':
    # print(lf.__closure__)
    print('Global Message ::', message)
    scoping_rules()
    print('Global Message ::', message)
