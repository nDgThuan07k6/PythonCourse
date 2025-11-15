# Scope is the region that a variable is recognized
# A variable is only  available from inside the region it is called
# A global and local scoped versions of a variable can be created
def display_name():
    name = 'Nguyen'                     # This is a local scope (it is only available inside this function)
    print(name)
print(name)                             # Result: NameError: name 'name' is not defined

# Calling variable outside of the function it will available inside and outside function and the same time
name = 'Thuan'                          # This is a global scope (available inside and outside function)
print(name)                             # Result: Thuan