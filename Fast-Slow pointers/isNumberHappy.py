def isHappy(num):
    slow,fast=num,num

    while True:
        slow=squareSum(slow)
        fast=squareSum(squareSum(fast))

        if slow==fast:
            break

    return slow==1

def squareSum(num):
    sum=0
    while num>0:
        digit=num%10
        sum+=digit*digit
        num//=10

    return sum

print(isHappy(23))
