average_score = int(input('Enter your average score to print the result: '))
if average_score >= 0 and average_score <= 59:
    print('Result is Fail')
elif average_score <= 84:
    print('Result is Second class')
elif average_score <= 95:
    print('Result is First class')
elif average_score <= 100:
    print('Result is Excellent')
else:
    print('Invalid Score')