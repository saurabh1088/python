# LEGB

GLOBAL = "Global"
def example_function():
    ENCLOSING = "Enclosing"
    def inner_function():
        LOCAL = "Local"
        print(LOCAL)
        print(ENCLOSING)
        print(GLOBAL)
        print(len(LOCAL)) # Here len is a built-in function, so it will look in the built-in scope
    inner_function()


# This will work because Python does not have block scope.
# Python has function scope. So BLOCK_VAR is accessible outside the if block.
def block_scope_example_using_if():
    if True:
        IF_BLOCK_VAR = "If Block Variable"
    print(IF_BLOCK_VAR)

def block_scope_example_using_for():
    for i in range(1):
        FOR_BLOCK_VAR = "For Block Variable"
    print(FOR_BLOCK_VAR)

example_function()
block_scope_example_using_if()
block_scope_example_using_for()

