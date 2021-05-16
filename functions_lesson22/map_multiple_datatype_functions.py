def fun(list1,tup1):
    return list1+" "+tup1

def main():
    list1 = ['e','f','g','h']
    tup1 = ('a','b','c','d')

    final = map(fun,list1,tup1)

    print(list(final))

if __name__ == '__main__':
    main()