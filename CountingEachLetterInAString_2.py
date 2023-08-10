from CountingEachLetterInAString import histogram 

def print_hist(h):
    for c in h:
        print(c, h[c])

h = histogram('попугай')
print_hist(h)