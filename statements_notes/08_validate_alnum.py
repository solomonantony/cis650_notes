while True:
        print('Select a new password (letters and numbers only):')
        password = input()
        if password.isalnum():
            break
        print('Passwords can only have letters and numbers.')
print(f'The password is {password}')
