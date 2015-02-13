#get input
num = int(input("Enter an integer (0-1000): "))

#process
total=0
x=num % 10
total=total+x
num = num // 10
x=num % 10
total= total + x
num = num //10
x =num % 10
total = total + x
num = num // 10

#output results
print(total)

