def main():

    f = open('test.txt','w+')

    for i in range(10):
        f.write('The New Line %d \n'% i)

    f.close()

if __name__ == '__main__':
    main()