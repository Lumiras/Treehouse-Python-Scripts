def first_last_four(iter):
    for things in iter:
        return iter[0:4] + iter[-4:len(iter)]

ranger = list(range(500))

print (first_last_four(ranger))
