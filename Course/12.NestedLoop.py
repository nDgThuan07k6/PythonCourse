rows = int(input('How many rows: '))
columns = int(input('How many colums: '))
symbol = input('Input symbol: ')

# The inner loop will finish all of it iteration before finish the outer loop
for i in range(rows):                   # After that is this loop
    for j in range(columns):            # Work in this loop first
        print(symbol, end=' ')          # Print symbol
    print()
