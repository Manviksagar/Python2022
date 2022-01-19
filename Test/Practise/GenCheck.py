
def gen():
    n=1
    while(n<10):
        sq=n*n
        yield sq
        n+=1


l=gen()
for i in l:
    print(i)


print(type(gen()))

def g():
    for i in range(10):
        yield i

for u in g():
    print(u)