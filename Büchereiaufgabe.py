books_total = 0
books_available = 0
error = "nicht ausreichent Bücher vorhanden"

def addBooks (quantity):
    global books_total
    global books_available
    total = books_total + quantity
    available = books_available + quantity
    books_total = total
    books_available = available
    print("Bücher total:", books_total)
    print("Bücher verfügbar:", books_available)

def lendBooks (quantity):
    global books_total
    global books_available
    if books_available >= quantity:
        available = books_available - quantity
        books_available = available
        print("Bücher verfügbar:", books_available)
    else:
        print(error)

def returnBooks (quantity):
    global books_total
    global books_available
    if books_total < books_available + quantity:
        total = books_total + quantity
        available = books_available + quantity
        books_available = available
        books_total = total
        print("Bücher total:", books_total)
        print("Bücher verfügbar:", books_available)
    else:
        available = books_available + quantity
        books_available = available
        print("Bücher total:", books_total)
        print("Bücher verfügbar:", books_available)

def checkAvailability ():
    global books_available
    print("Bücher verfügbar:", books_available)

def calculateAvailabilityPercentage():
    global books_total
    global books_available
    onepercent = books_total / 100
    currentavailability = books_available / onepercent
    print("Prozentualer Anteil verfügbarer Bücher:", currentavailability, "%")

addBooks(1)
addBooks(3)
lendBooks(3)
returnBooks(6)

checkAvailability()

calculateAvailabilityPercentage()