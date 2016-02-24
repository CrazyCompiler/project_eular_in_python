
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

maxMultiplesOf3 = 1000/3
maxMultiplesOf5 = 1000/5
sum=0
index = 1;

while index<=maxMultiplesOf3:
    sum+=index*3
    index += 1

index=1

while index<maxMultiplesOf5:
    if index%3!=0:
        sum+=index*5
    index += 1

print sum
