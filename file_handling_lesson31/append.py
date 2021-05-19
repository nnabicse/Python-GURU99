def main():
    f = open('test.txt','a+')
    for i in range(3):
        f.write('Appended Line %d \n'% i)

if __name__ == '__main__':
    main()