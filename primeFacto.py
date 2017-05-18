#!/bin/env python


def primefacto(x):
    div = 2
    while div < x:
        if x % div == 0:
            x /= div
            div -= 1
        div += 1
    return x


def main():
    num = 600851475143
    print primefacto(num)


if __name__ == '__main__':
    main()
