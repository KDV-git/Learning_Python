var = 0


def local():
    var = 100


def glob1():
    global var
    var += 1


def glob2():
    var = 0
    import ch_17_1_global_scopes_test
    ch_17_1_global_scopes_test.var += 1


def glob3():
    var = 0
    import sys
    glob = sys.modules['ch_17_1_global_scopes_test']
    glob.var += 1


def test():
    print(f'var is {var}')
    local()
    glob1()
    glob2()
    glob3()
    print(f'var is {var}')
