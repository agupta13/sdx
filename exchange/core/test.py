import os, sys

class foo:
    x=1

class bar(foo):


    def get_test(self):
        return foo.x


    def set_test(self,y):
        foo.x=y

class test(bar):
    y=1

def main():
    t=test()
    p=test()
    print t.x
    t.set_test(2)
    print t.x
    p.set_test(3)
    print t.x

    print 'hello'
    print t.x


if __name__=="__main__":
    main()