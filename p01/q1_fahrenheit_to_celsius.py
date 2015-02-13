#Write a program q1_fahrenheit_to_celcius.py
#that reads a Fahrenheit degree in double
#(floating point / decimal) from standard input
#then converts it to Celsius and displays the
#result in standard output
#The formula for the conversation is as follows:
#celsius = (5/9) * (fahrenheit - 32)

#get input
fahrenheit = float(input("Enter Fahrenheit degree: "))

#process
celsius = (5/9) * (fahreneit - 32)

#output results
print("celsius = {0:.1f}", format(celsius))