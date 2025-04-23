print(dir(__builtins__))
number = 42
dir()

def double_number(number):
    result = number * 2
    print(dir())
    return result

print(double_number(4))

global_variable = "global"

def outer_func():
    nonlocal_variable = "nonlocal"
    def inner_func():
        local_variable = "local"
        print(f"Hi from the '{local_variable}' scope!")
        print(f"Hi from the '{nonlocal_variable}' scope!")
        print(f"Hi from the '{global_variable}' scope!")
    inner_func()
outer_func()

x = "global"

def outer():
    def inner():
        print(x)
    inner()
outer()

x = "global"
def outer():
    x = "enclosing"
    def inner():
        print(x)
    inner()

outer()

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
outer()

list = [1,2,3,4]
print(list)

# print(list(range(10))) : Throws error
del list
print(list(range(10)))
list = [1,2,3,4]
import builtins
print(builtins.list(range(10)))
print(type(globals()))
print(globals())
number = 42
print(globals())
print(number)
print(globals()["number"])
print(number is globals()["number"])
globals()["message"] = "Welcome to Real Python!"
print(globals())
print(message)
globals()["message"] = "Hello, World!"
print(message)

def func(x, y):
    message = "Hello!"
    print(locals())

func(10, 0.5)
print(locals())
print(globals())
print(locals() is globals())

def func():
    message = "Hello!"
    loc = locals()
    print(f"{loc = }")
    number = 42
    print(f"{loc = }")
    loc['message'] = "Welcome!"
    print(f"{loc = }")
    print(f"{locals() = }")
func()

def func():
    fruits = ["apple", "banana"]
    loc = locals()
    loc["fruits"].append("orange")
    print(f"{loc = }")
    print(f"{locals() = }")
func()

x = 20
def f():
    x = 40
    print(x)
f()
print(x)
# In contrast, a function can modify a mutable object from an outer scope
# In this example, fruits is a list, and lists are mutable. You can change the list’s content inside f() even though the list is defined outside the function’s scope.
fruits = ["apple", "banana", "cherry", "mango"]
def f():
    fruits[1] = "peach"

f()
print(fruits)

fruits = ["apple", "banana", "cherry", "mango"]
def f():
    fruits = ["grapes", "orange"]
f()
print(fruits)

x = 20
def f():
    global x
    x = 40
    print(x)

f()
print(x)
x = 20
def f():
    globals()["x"] = 40
    print(x)
f()
print(x)

def f():
    global y
    y = 20

f()
print(y)

x, y, z = 10, 20, 30
def f():
    global x, y, z

def f():
    x = 20
    def g():
        nonlocal x
        x = 40
    g()
    print(x)

f()