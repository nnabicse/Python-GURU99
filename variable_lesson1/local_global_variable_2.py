f = 101      # Define Global Variable
print(f)

def somefunction():
    global f            #Reference Global Variable f in function using Global Keyword
    print(f)

somefunction()
print(f)                # print global Variable f
