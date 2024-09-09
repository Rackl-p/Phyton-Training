
n = 15


count_row = []

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0: # muss zuerst kommen, da sonst die anderen Argumente zuerst greifen
        count_row.append('FizzBuzz')
    elif i % 3 == 0:
        count_row.append('Fizz')
    elif i % 5 == 0:
        count_row.append('Buzz')
    else:
        count_row.append(i)


print (count_row)