def main():
    import queue

    q1 = queue.Queue(20)

    for i in range(20):
        q1.put(i)

    print(list(q1.queue))

if __name__ == '__main__':
    main()