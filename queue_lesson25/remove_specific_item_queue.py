def main():
    import queue

    q1 = queue.Queue(20)

    for i in range(20):
        q1.put(i)
    print(list(q1.queue))

    while not q1.empty():
        print('The Value To remove: ',q1.get())

if __name__ == '__main__':
    main()