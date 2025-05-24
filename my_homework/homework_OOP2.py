

# 1 Полиморфизм через переопределение метода

class Animal:

    def make_sound(self):
        print("some sound")


class Dog(Animal):

    def make_sound(self):
        return "Woof Woof"


class Cat(Animal):

    def make_sound(self):
        return "Meow Meow"

animal = [Dog(), Cat()]
for i in animal:
    print(i.make_sound())


# 2 Полиморфизм через аргументы

class Person:
    def say_hello(self):
        return "Hello I'm person"


class Robot:
    def say_hello(self):
        return "Say Hello i'm robot"


def greet(anybody):
    print(anybody.say_hello())

Anna = Person()
greet(Anna)
tg_bot = Robot()
greet(tg_bot)


# 3 Полиморфизм через списки объектов

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Rectangle(5, 7),
    Circle(5),
    Triangle(7, 3)
]

for shape in shapes:
    print(shape.area())


# 4 Полиморфизм в методах с одинаковым названием


class EnglishTeacher:
    def teach(self):
        print("I like teaching English: grammar, vocabulary.")


class MathTeacher:
    def teach(self):
        print("I like teaching Math: algebra, geometry.")

teachers = [EnglishTeacher(), MathTeacher()]

for i in teachers:
    i.teach()


# 5 Модель платежей

class CreditCard:
    def pay(self, amount):
        print(f"Оплата {amount} через ==> Credit Card")


class PayPall:
    def pay(self, amount):
        print(f"Оплата {amount} через ==> PayPall")


class Bitcoin:
    def pay(self, amount):
        print(f"Оплата {amount} через ==> Bitcoin")

def process_system(payment_sysytem, amount):
    payment_sysytem.pay(amount)

cc = CreditCard()
pp = PayPall()
btc = Bitcoin()

process_system(cc, 150)
process_system(pp, 250)
process_system(btc, 0.0005)


# 6 Уведомления в разных форматах

class EmailNotification:
    def send(self, massage):
        print(f"Email: {massage}")


class SMSNotification:
    def send(self,massage):
        print(f"SMS: {massage}")


class PushNotification:
    def send(self, massage):
        print(f"Push: {massage}")

ntf = [EmailNotification(), SMSNotification(), PushNotification()]
message = "Ваш заказ прибыл можете забрать в ПВЗ"

for i in ntf:
    i.send(message)


# 7 Кнопки в GUI

class Button:
    def on_click(self):
        print("button")


class SaveButton:
    def on_click(self):
        print("save")


class CancelButton:
    def on_click(self):
        print("cancel")


class DeleteButton:
    def on_click(self):
        print("Delete")


buttons = [SaveButton(), CancelButton(), DeleteButton()]
for btn in buttons:
    btn.on_click()


# 8 Животные с разными реакциями

class Cat:
    def react_to(self, sound):
        if sound == "высокий":
            print("Кошка убегает")
        elif sound == "громкий":
            print("Кошка раздражается")
        else:
            print("Кошка не обращает внимания")



class Dog:
    def react_to(self, sound):
        if sound == "высокий":
            print("Собака настараживается")
        elif sound == "громкий":
            print("Собака начинает лаять")
        else:
            print("Собака отдыхает и лежит")


class Bird:
    def react_to(self, sound):
        if sound == "высокий":
            print("Птица сразу улетает")
        elif sound == "громкий":
            print("Птица пугается и прячется")
        else:
            print("Птица спокойно сидит")

animals = [Cat(), Dog(), Bird()]
sounds = ["высокий", "громкий", "тихий"]

for sound in sounds:
    print(f"\nЗвук: {sound}")
    for animal in animals:
        animal.react_to(sound)


# 9 Применение скидки

class RegularCustomer:
    def apply_discount(self, price):
        return price * 0.9


class PremiumCustomer:
    def apply_discount(self, price):
        return price * 0.7


class StudentCustomer:
    def apply_discount(self, price):
        return price * 0.8

customers = [RegularCustomer(), PremiumCustomer(), StudentCustomer()]
price = 1000

for i in customers:
    final_price = i.apply_discount(price)
    print(f"Цена со скидкой : {final_price}")
    
    
# 10 Система печати документов

class PDFPrinter:
    def print(self, document):
        print(f'PDF: {document}')

class WordPrinter:
    def print(self, document):
        print(f'Word: {document}')

class ImagePrinter:
    def print(self, document):
        print(f'Image: {document}')

pdf = PDFPrinter()
word = WordPrinter()
image_3gp = ImagePrinter()

pdf.print("отчет.pdf")
word.print("доклад.docx")
image_3gp.print("фото.png")
