def squre(x):
    return x*x

def main():
    y = [1,2,3,4,5,6,7,8,9]
    z = map(squre,y)
    print(list(z))

if __name__ == '__main__':
    main()