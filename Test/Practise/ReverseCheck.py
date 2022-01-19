n=123
rev=0
while(n!=0):
    rev=rev*10+n%10
    n=n//10
print(rev)


#for loop testing over

s=[x if x%5==0 else x for x in range(20)]

print(s)

i=1
while(i<=10):

    print(i)
    i+=1