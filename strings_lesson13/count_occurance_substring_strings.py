def main():
    str = 'welcome to python python python tutorials and py'
    strcount = str.count('py')
    print(strcount)

    strcount1 = str.count('py',0,31)
    print(strcount1)

if __name__ == '__main__':
    main()