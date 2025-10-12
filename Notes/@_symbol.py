# @ symbol

# A decorator is a function that takes another function as an argument, adds some functionality to it, and returns a
# new function.


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()

# 	-- When you call say_hello(), the output will be:
#
# 	Something is happening before the function is called.
# 	Hello!
# 	Something is happening after the function is called.
#
#
# Defining the Decorator Function:
#
# my_decorator is a function that takes another function func as its argument.
#
# Inside my_decorator, we define an inner function wrapper that adds some behavior before and after calling func.
#
# wrapper calls func and then performs additional actions.
#
# The my_decorator function returns the wrapper function.
#
# Applying the Decorator:
#
# The @my_decorator syntax is a shorthand for applying the decorator to the say_hello function.
#
# This is equivalent to writing say_hello = my_decorator(say_hello).


"""+++++++++++++++++++++++++++"""


# 1. Basics of @property Decorator The @property decorator in Python allows you to define methods in a class that can
# be accessed like attributes. This means you can encapsulate instance variables and provide controlled access to
# them without changing the external interface of your class.
#
# 2. Defining Getter Method The primary use of @property is to define getter methods. Here's how you can define a
# simple class with a getter method:
#


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    # In this example:
    #
    # The radius method is decorated with @property, making it accessible like an attribute.
    #
    # Accessing c.radius will invoke the radius method without explicitly calling it as a method (i.e.,
    # without parentheses).
    #
    # 3. Adding Setter Method In addition to getting the value, you may want to allow setting the value with some
    # validation. This is done using the @property_name.setter decorator:

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    # 4. Adding Deleter Method
    # You can also define a method to delete the property using the @property_name.deleter decorator:

    @radius.deleter
    def radius(self):
        print("Deleting radius")
        del self._radius

# The radius method with @radius.deleter allows you to delete the property using del c.radius.
