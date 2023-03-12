#  While loop to prompt the user again and again for valid input
while True:
    # try block to see if user enter valid age
    try:
        name = input('What is your name: ')
        # if name is not string, program will prompt the user to enter a valid name
        if not name.isalpha():
            print('Invalid Input: please enter a name. ')
            continue
        # if name is string the program will continue
        else:
            pass
        # Asking user to enter the age
        age = int(input('How old are you? '))
        # if user enter correct age program will discontinue the while loop
        break
    #  except block if user has enter invalid age to give invalid input message
    except ValueError:
        print('Invalid Input: you need to enter number for age')
        print()
# calculate to year of birth
birthYear = 2023 - age

print(f'Hello {name.capitalize()}! You were born in {birthYear}.')
