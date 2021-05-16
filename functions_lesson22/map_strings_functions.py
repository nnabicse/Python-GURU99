def func(str):
    return str.upper()

def main():
    x = 'Welcome to tamim99 tutorials'
    y = map(func,x)

    for i in y:
        print(i,end='')

if __name__ == '__main__':
    main()