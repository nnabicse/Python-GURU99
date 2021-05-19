def display():
    print('East Delta University')

def main():
    from threading import Timer

    t = Timer(5,display)

    t.start()

if __name__ == '__main__':
    main()