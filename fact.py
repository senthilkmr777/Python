def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(fact(n))
