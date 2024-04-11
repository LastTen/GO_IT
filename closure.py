def make_multiplier_of(n):
    def multiplier(x):
        return x * n

    return multiplier


# Множник 3
print(make_multiplier_of(3)(2))

# Множник 5
times5 = make_multiplier_of(5)

# Вивід значень

print(times5(3))
