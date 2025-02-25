def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)

def fibon(n):
    if n <= 1:
        return n
    return fibon(n-1) + fibon(n-2)


def digit_sum(n):
    if n == 0:  # Base case: If the number is 0, return 0
        return 0
    return digit_sum(n // 10) + (n % 10)  # Recursive case: sum of digits

if __name__ == '__main__':
    print(fac(4))
    print(fibon(10))
    print(digit_sum(12345))  # Output: 15 (1+2+3+4+5)
