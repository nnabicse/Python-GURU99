class myclass():
    def method1(self):
        print('guru99')
    def method2(self,somestring):
        print('SWE Test:'+ somestring)
class childclass(myclass):
    def method3(self):
        print('Child Class Method')

def main():
    c=myclass()
    d=childclass()
    c.method2('Testing is fun')
    d.method1()
    d.method3()

if __name__ == '__main__':
    main()