f = 101  # f is declared as global scope
print(f)


def somefunction():
    f = 'I am learning Cobra'  # f is now declared as local scope
    print(f)


somefunction()  # f for local scope only works for the function
print(f)        # f for local scope not works for rest of the code outside the function
                # This f will return the global value
