
while True:
    try:
        age = int(input('What is your age? '))
        print(10/age)
    except ValueError:
        print('Enter a number')

    except ZeroDivisionError:
        print('Enter a number more than zero!')

    else:
        print('Thank you!')
        break


