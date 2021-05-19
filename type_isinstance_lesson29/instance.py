def main():
    age = isinstance(51,int)
    print('age is an intiger',age)

    pi = isinstance(3.1416,float)
    print('Pi is Float: ',pi)

    class myclass:
        m = 'Hello'
    c = myclass()
    print('C is a instance of myclass: ',isinstance(c,myclass))

if __name__ == '__main__':
    main()