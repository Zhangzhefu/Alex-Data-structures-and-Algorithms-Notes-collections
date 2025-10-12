# I didn't know how this worked until now, check out codecademy if forgotten
class Employee():
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("my id is {}.".format(self.id))


# overwrite definition
class Admin(Employee):
    def say_id(self):
        super().say_id()  # using super(), calls the parent class's
        # def and move it down here for use
        print("I'm a admin")


class Manager(Admin):
    """multiple inheritance 1, 2 is ext file"""

    def say_id(self):
        super().say_id()
        print("I'm in charge")


# polymorphism
meeting = [Employee(), Admin(), Manager()]
for member in meeting:
    member.say_id()

# e1 = Employee()
# e2 = Employee()
# e1.say_id()
# e2.say_id()
# e3 = Admin()
# e3.say_id()
# e4 = Manager()
# e4.say_id()
