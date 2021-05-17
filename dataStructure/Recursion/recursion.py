# -*- coding:utf-8 -*-

def f1(n):

    if n == 1:
        return 1

    return f1(n-1)+1


def f2(n):

    if n == 1:
        return 1

    if n == 2:
        return 1

    return f2(n-1) + f2(n-2)

if __name__ == '__main__':
    print(f1(4))
    print(f2(4))

