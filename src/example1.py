# import sys

print("ou")


# def sqrt(x):
#
#     if x < 0:
#         raise ValueError("Errore, il valore {} è negativo.".format(x))
#
#     guess = x
#     i = 0
#     while guess * guess != x and i < 20:
#         guess = (guess + x / guess) / 2.0
#         i += 1
#     return guess
#
#
# def main():
#     try:
#         print(sqrt(-2))
#     except ValueError as e:
#         print(e, file=sys.stderr)
#
#
# if __name__ == '__main__':
#     main()

def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


if __name__ == '__main__':
    run_take()
