last_name = input('What is your last name? ')
initial = last_name[0].upper()
homeroom = 101 if initial in ('A', 'B', 'C', 'D', 'E', 'F', 'G') else (102 if initial in ('H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P') else 103)

print(homeroom)