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

def result_type_of_functions_without_any_return():
    # The return value of a function without a return statement is None.
    # The output of the below print statement will be None.
    output = sample_function_not_returning_any_value()
    if output is None:
        print("Output of sample_function_not_returning_any_value() is None")
        print(type(output))

def usage_as_variable_initialisation():
    # None can be used to initialise a variable. Here object is initialised with None till it is assigned a value.
    object = None
    print(object)
    print('Assigning value to object...')
    object = 10
    print(f'Value of object is {object}')

def usage_as_in_boolean_context():
    # None is considered as False in a boolean context.
    if None:
        print("None is True")
    else:
        print("None is False")

def sample_function_not_returning_any_value():
    pass

