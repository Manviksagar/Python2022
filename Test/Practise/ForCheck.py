ls=[i for i in range(1,21) if i%2==0]

print(ls)

di=[int(x/2) for x in ls]

print(di)
num=input("enter the desired number: ")
if (int(num) in di):
    print("Available in list")

else:
    print("not avaible")


