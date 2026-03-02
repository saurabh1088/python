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

example_function()
