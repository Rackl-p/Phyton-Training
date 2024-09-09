#def asterix(n):
#    for i in range(0, n):
#        print((i+1) * "+")

#asterix(3)

def asterix(reihen):
    for i in range(reihen):
        print(' ' * (reihen - i - 1) + '*' * (2 * i + 1))
    #i = i - 4
    #print(i)
    for i in range(reihen - 2, -1, -1):
        print(' ' * (reihen - i - 1) + '*' * (2 * i + 1))

asterix(10)

# von Maggus
#def asterix(n):
#    for i in range(0, n):
#        print((' ' * (n - i)) + ('*' * i) + ('*' * (i - 1)))
#    for i in range(1, n):
#       print((' ' * i) + ('*' * (n - i)) + ('*' * ((n - i) - 1)))
#

#asterix(10)