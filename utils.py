import math
def factorial(n):
return math.factorial(n)

def is_prime(n): if n<2:
return False
for i in range(2, int(n**0.5)+ 1):
if n%i == 0:
return False
return True

def is_power_of_five(n):
while n > 1 and n % 5 == 0:
n //= 5
return n == 1
