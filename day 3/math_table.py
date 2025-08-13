import sys

number = int (sys.argv[1])
print(f'user given number is{number}')


for i in range(1,21):
    print('%d * %d = 3%d ' % ( number , i , number * i))
    #print(f'{number} * {i} = {number * i}')