def func(x):
    return x*5
def main():
    y = {2,3,4,5,6,7,8,9}
    z = map(func,y)

    print(z)
    print(list(z))


if __name__ == '__main__':
    main()