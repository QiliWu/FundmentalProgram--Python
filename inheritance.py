class Parent(object):
    def __init__(self, last_name, eye_color):
        print('Parent constructor called')
        self.last_name = last_name
        self.eye_color = eye_color

billy_cyrus = Parent('Cyrus','blue')
print(billy_cyrus.last_name)

class Child(Parent):
    def __init__(self, last_name, eye_color, numbers_of_toys):
        print('Child constructor called')
        Parent.__init__(self, last_name, eye_color)
        self.numbers_of_toys = numbers_of_toys

miley_cyrus = Child('Cyrus','gray','5')
print(miley_cyrus.last_name)
print(miley_cyrus.numbers_of_toys)