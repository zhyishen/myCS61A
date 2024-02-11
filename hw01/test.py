def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    i = 1
    while n>1:
        if n%2 == 0:
            print(n)
            n //= 2
            i += 1
        else:
            print(n)
            n = 3*n +1
            i += 1
    print(n)
    return i
    


