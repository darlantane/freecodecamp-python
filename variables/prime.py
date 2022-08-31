user_input = input('enter a number')
user_input = int(user_input)


for i in range(2, user_input-1):
    if user_input % i == 0:
        print('this number isn t prime')
    else:
        print('this number is prime')
