def main():
    arg = input("Enter Argument: ")

    switcher = \
        {
            0: 'This case is 0',
            1: 'This case is 1',
            2: 'This case is 2',
        }
    print(switcher[int(arg)])

if __name__ == '__main__':
    main()

