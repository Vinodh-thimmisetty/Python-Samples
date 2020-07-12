"""
    Modeling Shipping Container - Python Object Oriented Programming

    -   use `__` for avoiding accessing variables/methods outside the module.
        prefer setters/getters using `@property` & `p_name.setter`
    -   use `@classmethod` for parameterized constructors.
        Make sure to pass *args (or/and) **kwargs for sub-classes to use @classmethod

    a) 'cls' attributes must refer and modify based on Class Name.
    b) Avoid `cls` variables access using `self` which creates local attribute with same name.
    c) Have Class invariants (validations)
    d) Don't override @property, instead delegate and override to instance methods.

"""


def generate_bic_code(owner_code, serial_number, category='U'):
    """
        Bureau International Container = BIC code ISO-6346 format
        eg: CSQ{owner_code} U{Category Identifier} 305438{serial_number} 3{check digit}
    """
    from random import randint
    return ''.join(
        [
            str(owner_code[:3]).upper(),
            str(category),
            str(serial_number).zfill(6),
            str(randint(1, 9))
        ])


class ShippingContainer:
    next_serial_number = 1000

    @staticmethod  # no-knowledge about it's class or instance is.
    def __generate_serial():
        print(f'@staticmethod  `generate_serial` called')
        cur_serial_number = ShippingContainer.next_serial_number
        ShippingContainer.next_serial_number += 1
        return cur_serial_number

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return generate_bic_code(owner_code, serial)

    @classmethod  # factory method - 1
    def empty(cls, owner_code, *args, **kwargs):
        print(f'@classmethod `empty` called')
        return cls(owner_code, [], *args, **kwargs)

    @classmethod  # factory method - 2
    def sports(cls, *args, **kwargs):
        print(f'@classmethod `sports` called')
        # cls.next_serial_number
        return cls('Vinodh', ['football', 'cricket'], *args, **kwargs)

    @classmethod
    def pre_load_container(cls, owner_code, *args):
        return cls(owner_code, contents=args)

    def __init__(self, owner_code, contents, category='U', *args, **kwargs):
        print(f'ShippingContainer __init__ method called')
        self.__owner_code = owner_code
        self.contents = contents
        self.category = category
        self.bic_code = self._make_bic_code(  # overriding the @staticmethod to enable polymorphism
            owner_code=owner_code,
            serial=ShippingContainer.__generate_serial()
        )

    @property
    def owner_code(self):
        return self.__owner_code

    @owner_code.setter
    def owner_code(self, owner_code):
        self.__owner_code = owner_code


def cel_to_fah(cel):
    return round(((cel * 9 / 5) + 32), 2)


def fah_to_cel(fah):
    return round(((fah - 32) * 5 / 9), 2)


class RefrigeratedContainer(ShippingContainer):
    """
        Category = 'R'
    """

    MAX_CELSIUS = 4.0  # constant

    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code, contents, **kwargs)
        if celsius > RefrigeratedContainer.MAX_CELSIUS:
            raise ValueError(f'Temperature too hot')
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, celsius):
        if celsius > RefrigeratedContainer.MAX_CELSIUS:
            raise ValueError(f'Temperature too hot')
        self.__celsius = celsius

    @property
    def fahrenheit(self):
        return cel_to_fah(self.__celsius)

    @fahrenheit.setter
    def fahrenheit(self, fahrenheit):
        celsius = fah_to_cel(fahrenheit)
        if celsius > RefrigeratedContainer.MAX_CELSIUS:
            raise ValueError(f'Temperature too hot')
        self.celsius = celsius

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return generate_bic_code(owner_code, serial, category='R')
