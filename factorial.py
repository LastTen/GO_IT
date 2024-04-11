def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    n_fac = factorial(n)
    nk_fac = factorial(n - k)
    k_fac = factorial(k)
    return int(n_fac / (nk_fac * k_fac))


print(number_of_groups(33, 7))
