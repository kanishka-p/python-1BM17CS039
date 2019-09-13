output = ""
with open('f1.txt','r') as f:
    i=0
    l=len(f.read())
    while i<(l-1) : 
        f.seek(l-2-i)
        output+=f.read(1)
        i=i+1
print(output)       



