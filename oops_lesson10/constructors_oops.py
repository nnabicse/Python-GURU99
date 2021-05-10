class user:
    name = ''

    def __init__(self,name):
        self.name = name

    def sayhello(self):
        print('Welcome '+self.name)

def main():
    user1 = user('Alex')
    user1.sayhello()


if __name__ == '__main__':
    main()

