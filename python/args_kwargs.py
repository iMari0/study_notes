#Args
    # Use '*' to define arguments
def add(*num):
    sum = 0

    for n in num:
        sum = sum + n

    print("Sum: ", sum)

add(1,2)
add(4,5,6,6,7)

#kwargs

def intro(**kwargs):
    print("\nData type of argument:", type(kwargs))

    for key, value in kwargs.items():
        print("{} is {}".format(key,value))

intro(Firstname = 'Mario', Lastname = "Iuliano", Age = '34')
intro(Firstname = 'Sophie', Lastname = "Trommler")
