def main():
    list=['siya','tiya','guru','daksh','riya','guru']
    i = 0

    while True:
        print(list[i])
        if list[i]=='guru':
            print('guru found')
            break
        i+=1
    print('loop terminated')

if __name__ == '__main__':
    main()