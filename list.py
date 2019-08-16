li = []
li1 = []
n=int(input("enter the number"))
for i in range(0,n):
  ele=int(input("enter the elements"))
  li.append(ele)
for num in li:
   if num%2==0:
      li1.append(num)
print(li1)
