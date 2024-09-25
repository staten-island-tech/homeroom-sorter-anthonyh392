last_name = input('What is your last name? ')
initial = last_name[0].upper()
homeroom = 101 if initial == 'A' else (102 if initial == 'B' else 103)

print('Your homeroom:', homeroom)