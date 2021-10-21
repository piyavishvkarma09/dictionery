a="MISSISSIPPI"
k={}
for i in a:
    if i not in k:
        k[i]=1
    else:
        k[i]=k[i]+1
print(k)