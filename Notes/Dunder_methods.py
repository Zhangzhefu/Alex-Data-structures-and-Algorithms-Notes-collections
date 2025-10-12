"""Dunder/magic methods in Python"""
"""Basic"""


class Rectangle:
    def __init__(self, x, y):
        """Used to construct or create a new object"""
        self.x = x
        self.y = y


Rectangle(2, 3)  # Automatically calls the __init__ function and pass those values into them

"""Arithmetic and comparison"""


class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"InventoryItem(name={self.name}, quantity={self.quantity})"

    def __add__(self, other):
        """Allows to be added"""
        if isinstance(other, InventoryItem) and self.name == other.name:
            return InventoryItem(self.name, self.quantity + other.quantity)
        raise ValueError("Incorrect types")

    def __sub__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            if self.quantity >= other.quantity:
                return InventoryItem(self.name, self.quantity - other.quantity)
            raise ValueError("Cannot subtract more than available")
        raise ValueError("Incorrect types")

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return InventoryItem(self.name, int(self.quantity * factor))
        raise ValueError("Incorrect type")

    def __truediv__(self, factor):
        if isinstance(factor, (int, float)) and factor != 0:
            return InventoryItem(self.name, self.quantity / factor)
        raise ValueError("No zeros!")

# Comparison
    def __eq__(self, other):
        if isinstance(other, InventoryItem):
            return self.name == other.name and self.quantity == other.quantity
        return False

    def __lt__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quantity < other.quantity
        raise ValueError("Incorrect types")

    def __gt__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quantity < other.quantity
        raise ValueError("Incorrect types")


item1 = InventoryItem("Apple", 30)
item2 = InventoryItem("Apple", 50)
item3 = InventoryItem("Banana", 20)

results_add = item1 + item2
print(results_add)

results_sub = item2 - item1
print(results_sub)

result_mul = item1 * 3
print(result_mul)

print(item1 > item2)


"""######################################"""
"""Representation"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        """Meant for user"""
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self):
        """Meant for a more detailed, unambiguous output, more for developers"""
        return f"Car(make='{self.make}', model='{self.model}', year='{self.year}')"


my_car = Car('Toyota', 'Sienna', 2017)

print(str(my_car))
print(repr(my_car))


"""Indexing"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def __delitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Out of range")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def __contains__(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(len(ll))
print(ll[1])
ll[2] = 44
print(ll)
del ll[1]
print(ll)
print(30 in ll)


"""Context managers"""


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        """Establish connection"""
        self.connected = True
        print(f"Connected to the database {self.db_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close connection"""
        self.connected = False
        print(f"Disconnected from database: {self.db_name}")
        if exc_type:
            print(f"Exception: {exc_val}")
        return True


with DatabaseConnection("ExampleDB") as db:
    print(f"Is connected? {db.connected}")


"""Iterators"""


class Countdown:
    def __init__(self, start):
        """Simple iterator that counts down from given number"""
        self.current = start

    def __iter__(self):
        """Returns the iterator object itself"""
        return self

    def __next__(self):
        """Returns the next value in the countdown"""
        if self.current > 0:
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration


for number in Countdown(5):
    print(number)
