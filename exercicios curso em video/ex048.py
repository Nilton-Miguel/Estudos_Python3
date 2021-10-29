r = 0

for n in range(1, 501):
    if not n % 2 == 0:
        if n % 3 == 0:
            r += n
print(r)
