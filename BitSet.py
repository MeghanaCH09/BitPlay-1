def nob(num, n):
    if(n&(1<<n-1)):
        print("SET")
    else:
        print("NOT SET")

num=int(input("Enter a number: "))
n=int(input("Enter a bit position: "))
nob(num, n)