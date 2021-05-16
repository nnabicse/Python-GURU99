def func (x):
    return x.upper()

def main():
    y = ('tamim','is','a','good','boy')
    x = map(func,y)

    print(list(y))

if __name__ == '__main__':
    main()