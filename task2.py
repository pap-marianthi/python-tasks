x = int(input("Enter a number: "))
factors = []
i = 2
while x > 1:
    #remainder of the division of n by i
    if x % i == 0:
        x = x / i
        factors.append(i)
    else:
        i += 1
#print(factors)

times = [[t,factors.count(t)] for t in set(factors)]
times = sorted(times, key = lambda x: (x[0], x[1]))
#print(times)

for i in times:
    a = i[0]
    b = i[1]
    #print("a=",a)
    #print("b=",b)
    print("(",a,"**",b,")", end = "")

#86240
