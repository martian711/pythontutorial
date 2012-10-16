import sys
def table1to10(num):
    for i in range(1,11):
        i=i*num
        print i
    return 0

def main():
    print 'Hello World. This is my First Program';
    a = 5
    if a == 5:
        a = a*5
    print a
if __name__ == '__main__':
    main()
    num = input('Enter your number')
    table1to10(num)
    print sys.argv[0]
