def grt():
    day = input('What is the day today:')
    print('the day today is'+ day)
# grt()


def courseunits(cs1, cs2, cs3):
    print('This semester I am doing these course units: ' + cs1 + ', ' + cs2 + ', ' + cs3)

cs1 = input('Enter cs1: ')
cs2 = input('Enter cs2: ')
cs3 = input('Enter cs3: ')
# courseunits(cs1, cs2, cs3)

# // arbituary aruments//

def lib(*books):
    for book in books:
        print(book)

# lib('django','java','enam','hrm')

# arbituary keyword arguments

def cars(**type) :
    for key,value in type.items():
        print(key,':',value)

# cars(benz='Gl', toyota='landcrusier',nissan='patrol')

if __name__ == '__main__':
    grt()
    courseunits(cs1, cs2, cs3)
    lib('django', 'java', 'enam', 'hrm')
    cars(benz='Gl', toyota='landcrusier', nissan='patrol')