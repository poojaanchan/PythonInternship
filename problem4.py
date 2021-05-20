a = int(input())
b = int(input())
c = int(input())
m3 = max(a,b,c)
m1 = min(a,b,c)
m2 = (a+b+c)-m1-m3

print(m3,m2,m1,sep=" > ")
