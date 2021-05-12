def main():
    str = 'Hello World'
    strcount = str.count('o')
    print(strcount)

    strcount1 = str.count('o',0,5)
    print(strcount1)

    srtcount2 = str.count('l',0,11)
    print(srtcount2)

if __name__ == '__main__':
    main()