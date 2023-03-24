num = int(input("Enter a number: ")) # count for total number of digits in a number
cnt=0
while num>0:
    cnt=cnt+1
    num//=10
print(cnt)