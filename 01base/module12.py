'test module'

__author__ = 'gh'


import sys

def test():
    s = sys.argv
    if len(s) == 1:
        print('Hello World')
    elif len(s) == 2:
        print('Hello %s' % s[1])
    else:
        print('many')

__gh__ = 'gh'
_gh_ = 'gh2'
gh = 'gh3'

def aa():
    print('aa')
    _aa()
    __aa()
def _aa():
    print('bb')
def __aa():
    print('cc')

if __name__ == '__main__':
    test()
    aa()
    _aa()
    __aa()