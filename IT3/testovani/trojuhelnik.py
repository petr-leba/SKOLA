def lze_sestrojit(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False
