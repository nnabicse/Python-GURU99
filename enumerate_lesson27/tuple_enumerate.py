def main():
    x = ('a','b','c','d','e','f','g','h','i','j','k','l')

    e_y = enumerate(x)

    print('\nUsing List: \n',list(e_y))

    print('\nUsing For Loop: \n')

    for i in enumerate(x):
        print(i)

if __name__ == '__main__':
    main()

