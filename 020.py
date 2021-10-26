input1 = int(input())
check = True
for i in range(2, input1):
    check = check and (input1 % i != 0)


if (check):
    print('{} is prime number'.format(input1))
else:
    print('{} is not prime number'.format(input1))
