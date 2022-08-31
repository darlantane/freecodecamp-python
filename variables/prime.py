user_input = input('enter a number')
user_input = int(user_input)

prime_flag = 0
if user_input > 1 :
    for i in range(2, user_input - 1):
        if user_input % i == 0:
            prime_flag = 1
            break
    if prime_flag == 0 :
        print("this number is prime")
    else:
        print("this number isn t prime")

else:
    print('this number isn t prime')
