# type annotations:

var1: int = 10


# adding the : and then enter the type {int} well lower future wrong type errors

def upper_everything(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]

