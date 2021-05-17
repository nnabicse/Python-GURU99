def fibonacci(num):
    c1 = 0
    c2 = 1
    count = 0

    while count<num:
        c3 = c1+c2
        yield c3
        c1 = c2
        c2 = c3
        count+=1

def main():
    num = 50
    p = fibonacci(num)

    #print(list(p))

    for i in p:
        print(i)
if __name__ == '__main__':
    main()
