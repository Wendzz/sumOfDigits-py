# Wendy Stump
# SDEV220
# Sum the digits of an integer using recursion
# 11/8/19

def sumDigits(n):
    if (n == 0):
        return 0
    else:
        return((n%10) + sumDigits(n//10))

def main():
    n = eval(input("Enter an integer to see its sum: "))
    print("The sum of", n, "is:", sumDigits(n))

main()
             
