# __contains__ method:

# In Python, the __contains__ method is a special method(also known as a "magic method" or "dunder method") that is
# used to define behavior for the in keyword.When you use the in keyword to check if an element is in a container (
# like a list, set, or dictionary), the __contains__ method is called internally.

# EXAMPLE:


class MyContainer:
    def __init__(self, elements):
        self.elements = elements

    def __contains__(self, item):
        return item in self.elements


my_container = MyContainer([1, 2, 3, 4, 5])

print(3 in my_container)  # Output: True
print(6 in my_container)  # Output: False

# In
# this
# example, the
# MyContainer


# class defines the __contains__ method, which checks if an item is present in the elements list.When you use the in
# keyword with an instance of MyContainer, it calls the __contains__ method to determine if the item is in the
# container.


# So, the __contains__ method allows you to customize the behavior of the in keyword for your custom objects,
# making your code more intuitive and expressive.
