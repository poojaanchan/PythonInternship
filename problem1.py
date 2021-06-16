N = int(input())
sum=0
if N>=3:
    for i in range(2,N+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            sum+=i
for num in range(2,sum):
    if sum%num==0:
        break
else:
    print(f"Satisfies the condition and the sum of all prime numbers is {sum}")