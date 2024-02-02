print("\nhttps://www.programiz.com/python-programming/methods/built-in/repr\n")

class Person:
    name = 'Adam'

    def __repr__(self):
        return repr('Hello ' + self.name )

print(repr(Person()))