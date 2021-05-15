def main():
    str = 'test string test, test string test, test string test'
    si = 0
    c = 0
    for i in range(len(str)):
        ssc = str.find('test',si)
        if (ssc !=-1):
            si = ssc + 1
            c +=1
            ssc = 0

    print('Total Count test: ',c)

if __name__ == '__main__':
    main()
