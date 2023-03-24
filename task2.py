#accept a list of a floating number as input from the user and display it
sz=int(input("Enter the size of a list :"))
lst=[] 
print("Enter the value of the list: ")
for i in range(0,sz):
    num= float(input()) 
    lst.append(num) 
print("The output  is: ")
print(lst)