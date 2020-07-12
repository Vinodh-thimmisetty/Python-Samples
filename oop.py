"""

    Object Oriented Programming:
        1) Encapsulation
            a) putting attributes & behavior of an object in single location
            b) don't let end-users directly change the attributes, instead provide setter/getter
            c)
        2) Inheritance
            a) categorization of similar objects
            b) Re-usability is the major benefit.Always, Provide common behavior to TOP-LEVEL category
        3) Polymorphism
            a) Same thing performed in different ways based on end-user requirement
            b) Duck Typing - if an object A behaves like object B, then A & B can be used interchangeably
            c) Dependency Injection - Dynamic passing of objects
            d) Compile[overloading] vs Runtime [overriding]
        4) Abstraction
            a) Define contract and let end-users know 'WHAT' an object can do and not 'HOW' to do
            b)

    1) Dynamically add/remove/modify the object properties
    2) object vs class vs instance vs static
    3) self --> instance; cls --> class; _ --> private [recommended]

    @classmethod - instead of letting end-user gather information for creating object,
                   we provide pre-built Factory-methods
                   e.g: For creating Circle class, we can have unit_circle() factory method which always has radius=1

    @staticmethod - bound to namespace but not class/instance.
                    math.* methods provide functionality independent of class

"""
from abc import abstractmethod, ABC


class Util:  # interface - all methods must be @abstractmethod

    @abstractmethod
    def max_allowed_students(self):
        pass

    @abstractmethod
    def whoami(self):
        pass


class Course(Util, ABC):  # abstract-class - one or more methods needs to be @abstractmethod's
    number_of_courses = 0  # class-level; access using ClassName is preferred instead of Instance

    def __init__(self, name, ratings):
        self._name = name  # instance-level
        self._ratings = ratings
        Course.number_of_courses += 1

    @staticmethod
    def total_courses():
        return Course.number_of_courses

    @property  # getter
    def name(self):
        return self._name

    @name.setter  # setter
    def name(self, name):
        self._name = name

    @property
    def ratings(self):
        return self._ratings

    def avg_rating(self):  # instance-methods
        return sum(self.ratings) / len(self.ratings)


class JavaCourse(Course):
    def max_allowed_students(self):
        return 100

    def whoami(self):
        # super().whoami()
        print(f'{JavaCourse.__name__}')


class PythonCourse(Course):
    def max_allowed_students(self):
        return 200

    def whoami(self):
        print(f'{PythonCourse.__name__}')


class PythonClass:

    def __init__(self):
        self._name = PythonClass.__name__
        print(f'object Instantiation')

    def instance_method(self):
        return f'instance method for - {self._name} - ' \
               f'can access the class - {self.__class__}', self

    @classmethod
    def class_method(cls):
        return f'class method for - {cls.__name__} - can modify all instances', cls

    @staticmethod
    def static_method():
        return f'static method - cannot access/modify class/instance',


if __name__ == '__main__':
    # react = Course('React', [])

    # java = JavaCourse('Java', [])
    # python = PythonCourse('Python', [])
    # print(Course.total_courses())
    #
    # java.whoami()
    # print(java.max_allowed_students())
    # python.whoami()
    # print(python.max_allowed_students())

    p = PythonClass()
    print(p.instance_method())
    print(p.class_method())
    print(p.static_method())
