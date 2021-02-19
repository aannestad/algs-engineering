f = open("sample.in", "r")
xs = list(map(int,f.read().split()))

for (x,y) in zip(xs[0::2],xs[1::2]):
    print(abs(x-y))