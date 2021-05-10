class myclass():
    def method1(self):
        print('guru99')
    def method2(self,somestring):
        print('SWE Test:'+ somestring)
def main():
    c=myclass()
    c.method1()
    c.method2('Testing is Fun')

if __name__ == '__main__':
    main()
