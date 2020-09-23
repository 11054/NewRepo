
scope = int(input("insert some number: ")) # 90


a = 0
b = 1
fib_number = 0
sum = 0

while fib_number < scope:
    
    fib_number = a + b
    if fib_number > scope:
        break
    a = b
    b = fib_number
    print(fib_number)
   
    if fib_number % 2 == 0:
        sum += fib_number

print("sum of the even-valued terms is:", sum)

    
        



        


