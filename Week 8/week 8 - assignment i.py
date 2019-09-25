#link for the question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=278

n=input()
s=n.split()
d=[]
for i in s:
  d.append(int(i))
a=[]
for i in d:
    if i not in a:
        a.append(i)
for j in range(len(a)-1):
    print(a[j],end=" ")
print(a[j+1],end="")
