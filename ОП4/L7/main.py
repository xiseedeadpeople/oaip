from factorial import factorial
from fibonacci import fibonacci
from vows import vows
from maximum import maximum
from simple import simple


def main():
    print(factorial(5))
    print(fibonacci(8))
    print(vows('raze'))
    print(simple('112'))
    print(maximum([2, 4, 6, 23, 1, 46]))


if __name__ == '__main__':
    main()
