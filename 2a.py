def func(li,num):
   if num in li:
       return 1
   else:
        return 0
li=[1,2,3,5,6,8]
num=int(input("enter the number"))
ans=func(li,num)
if ans==1:
    print("it is present in the list")
else:  
    print("it is not present")
