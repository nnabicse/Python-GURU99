def display():
    import time
    print("Display Function Executed After 6 Seconds")
    time.sleep(6)

def main():
    import time
    time.sleep(5)
    print('Main Function Delayed 5 Seconds')
    display()

if __name__ == '__main__':
    main()