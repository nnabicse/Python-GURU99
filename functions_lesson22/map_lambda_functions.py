def main():
    y = [1,2,3,4,5,6,7,8,9]

    z = map(lambda x:x*10, y)

    print(list(z))

if __name__ == '__main__':
    main()