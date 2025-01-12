def nob(n):
    ones=0
    zeros=0

    while(n):
        if(n&1==1):
            ones+=1
        else:
            zeros+=1
        n>>=1
    print(f"Number of ones are: {ones}")
    print(f"Number of zeros are: {zeros}")

num=int(input("Enter a value to get the number of Ones and Zeros: "))
nob(num)