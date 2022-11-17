#Encapsulation : provides the necessary data.
"""class Encapsulation():
    def __init__(self):
        pass
    def set_a_value(self,a):
        self.a=a
    def get_a_value(self):
        return self.a
        """
"""

#polymorphism:polymorphism is nothing but a function can do multiple functions(or)more types
               there are two types:1)static polymorphism(compile time)
                                   2)Dynamic polymorphism(run time)
      1)static polymorphism(compile time):single function can perform multiple task with single class.
                                         (or) perform multiple task in single function with single class.
      2)Dynamic polymorphism(run time):perform multiple task in single function with multiple classes.
                                                                      
               """
class A:
    def display_method(self):
        a=5
        print(a)

class B:
    def display_method(self):
        b=6
        print(b)



a=B()
a.display_method()
b=A()
b.display_method()