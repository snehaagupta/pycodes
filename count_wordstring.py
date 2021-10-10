mystr=input("Enter String:\n")
wrd=mystr.split()
count=dict()
for i in wrd:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)