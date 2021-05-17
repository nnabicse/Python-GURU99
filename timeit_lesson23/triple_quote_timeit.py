import_module = 'import random'
import timeit
testcode = '''    
def test():
    return random.randint(10,100)
'''
print(timeit.repeat(stmt=testcode,setup=import_module))
