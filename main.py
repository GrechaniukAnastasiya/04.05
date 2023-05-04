
def log_call(func):
    def wrapper(*args, **kwargs):
        returning = func(*args, **kwargs)
        print(f'Функція {func.__name__} приймає аргументи args {args}, '
              f'та kwargs {kwargs}, та повертає {returning}')
        return returning
    return wrapper
@log_call
def temperature(C):
    return (C * 1.8) + 32
print(temperature(32))
print(temperature(40))
print(temperature(50))
#Класи
class Student:
    print("Hi!")
    height = 190
    print(height)
    def __init__(self, height = 150):
        self.height = height
oleg = Student() #об'єкт, екземпляр класу
print(oleg.height)

class Student:
    print("Hi!")
    count = 0
    def __init__(self, height = 150):
        self.height = height
        Student.count += 1
oleg = Student() #об'єкт, екземпляр класу
print(oleg.height)
masha = Student(height = 200)
print(masha.height)
print(Student.count)
