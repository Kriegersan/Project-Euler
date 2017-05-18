#!/usr/bin/env python


def primeNumGen(x):
    fac = 1
    for i in range(2, x):
        fac *= i - 1
        if (fac + 1) % i == 0:
            yield i


def main():
    count = []
    prim = primeNumGen(110000)
    for i in prim:
        count.append(i)

    print count[10000]


if __name__ == '__main__':
    main()
