def type_of_none():
    return print(type(None))

def singleton_nature_of_none():
    objectOne = None
    objectTwo = None
    objectThree = None
    # The is keyword is used to test if two variables refer to the same object.
    # is operator checks for identity, meaning it determines whether two variables point to the same object in memory.
    # The output of the below print statement will be True, because None is a singleton.
    print(objectOne is objectTwo is objectThree)
