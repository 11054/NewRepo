
scope = int(input("input some number: "))
sum = 0

for x in range(scope):
    if (x % 3 == 0 or x % 5 == 0):
        print(x)
        sum += x
print(sum)
