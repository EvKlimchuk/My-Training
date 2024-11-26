def add_everything_up(a, b):
    try:

        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return round(a + b, 3)
        elif type(a) == type(b):
            return a + b
        else:
            raise TypeError("a and b have different types")
    except TypeError:
        return f"{a}{b}"




print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))