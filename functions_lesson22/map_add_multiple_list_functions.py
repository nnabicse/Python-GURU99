def fun(list1,list2):
    return list1+list2

def main():
    x = [1,2,3,4,5,6]
    z = [7,8,9,10,11]

    q = map(fun,x,z)

    print(list(q))

if __name__ == '__main__':
    main()