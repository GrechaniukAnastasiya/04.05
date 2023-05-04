'''
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
    def breathing(self): #методи класів
            return self.height - 10
oleg = Student() #об'єкт, екземпляр класу
print(oleg.height)
masha = Student(height = 200)
print(masha.height)
print(Student.count)
print(masha.breathing())
#Практична
#1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}")
student = Student("Vasia", 23)
student.info()
#2
class Circle:
    def __init__(self,radius):
        self.area = area
    def area(self):
            print(f" {area.}")
'''
class Animals:
    pass
class Dog(Animals):
    def sound(self):
        print("Гав")
bobik = Dog()
bobik.sound()